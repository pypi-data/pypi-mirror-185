"""
    lager.debug.commands

    Debug an elf file
"""
import click
from ..context import get_default_gateway
from ..debug.gdb import debug
from ..gateway.commands import _status


@click.group(name='debug')
def _debug():
    """
        Lager debug commands
    """
    pass

@_debug.command()
@click.pass_context
@click.option('--gateway', required=False, help='ID of gateway to which DUT is connected', hidden=True)
@click.option('--dut', required=False, help='ID of DUT')
@click.option('--mcu', required=False, default=None, help='MCU to query', type=click.INT)
def status(ctx, gateway, dut, mcu):
    gateway = gateway or dut
    _status(ctx, gateway, mcu)


@_debug.command()
@click.pass_context
@click.option('--gateway', required=False, help='ID of gateway to which DUT is connected', hidden=True)
@click.option('--dut', required=False, help='ID of DUT')
@click.option('--interpreter', '-i', required=False, default='default', help='Select a specific interpreter / user interface')
@click.option('--verbose', '-v', is_flag=True, default=False, help='Print verbose debug info')
@click.option('--tty', required=False, help='Use TTY for input/output by the program being debugged.')
@click.option('--quiet', '--silent', '-q', is_flag=True, default=False, help='Do not print the introductory and copyright messages. These messages are also suppressed in batch mode.')
@click.option('--args', required=False, help='Arguments passed to debugger')
@click.option('--ignore-missing/--no-ignore-missing', is_flag=True, default=True, help='Ignore missing files')
@click.option('--cwd', default=None, type=click.Path(exists=True, file_okay=False, resolve_path=True), help='Set current working directory')
@click.option('--cache/--no-cache', default=True, is_flag=True, help='Use cached source if ELF file unchanged', show_default=True)
@click.option('--mcu', required=False, default=None, help='MCU to query', type=click.INT)
@click.option('--elf-only', required=False, default=False, is_flag=True, help='Only send ELF file; no source')
@click.option('--debugfile', required=False, default=None, type=click.Path(), help='Debugger command file')
@click.argument('elf_file', type=click.Path())
def gdb(ctx, gateway, dut, interpreter, verbose, tty, quiet, args, ignore_missing, cwd, cache, mcu, elf_only, debugfile, elf_file):
    """
        Debug a DUT using an ELF file
    """
    gateway = gateway or dut
    debug(ctx, gateway, interpreter, verbose, tty, quiet, args, ignore_missing, cwd, cache, mcu, elf_only, debugfile, elf_file)


@_debug.command()
@click.pass_context
@click.option('--dut', required=False, help='ID of DUT')
@click.option('--mcu', required=False, help='MCU to connect')
@click.option('--force', is_flag=True, default=False, help='Disconnect debugger before reconnecting. If not set, connect will fail if debugger is already connected. Cannot be used with --ignore-if-connected', show_default=True)
@click.option('--ignore-if-connected', is_flag=True, default=False, help='If debugger is already connected, skip connection attempt and exit with success. Cannot be used with --force', show_default=True)
def connect(ctx, dut, mcu, force, ignore_if_connected):
    if force and ignore_if_connected:
        click.secho('Cannot specify --force and --ignore-if-connected', fg='red')
        ctx.exit(1)

    if dut is None:
        dut = get_default_gateway(ctx)
    session = ctx.obj.session
    resp = session.debug_connect(dut, mcu, force, ignore_if_connected).json()
    if resp.get('start') == 'ok':
        click.secho('Connected!', fg='green')
    elif resp.get('already_running') == 'ok':
        click.secho('Debugger already connected, ignoring', fg='green')

@_debug.command()
@click.pass_context
@click.option('--dut', required=False, help='ID of DUT')
@click.option('--mcu', required=False, help='MCU to disconnect')
def disconnect(ctx, dut, mcu):
    if dut is None:
        dut = get_default_gateway(ctx)
    session = ctx.obj.session
    session.debug_disconnect(dut, mcu).json()
    click.secho('Disconnected!', fg='green')

@_debug.command()
@click.pass_context
@click.option('--dut', required=False, help='ID of DUT')
@click.option('--mcu', required=False, help='MCU to erase')
def erase(ctx, dut, mcu):
    if dut is None:
        dut = get_default_gateway(ctx)
    session = ctx.obj.session
    out = session.debug_erase(dut, mcu).json()
    print(out['output'])
    click.secho('Erased!', fg='green')

@_debug.command()
@click.pass_context
@click.option('--dut', required=False, help='ID of DUT')
@click.option('--mcu', required=False, help='MCU to disconnect')
@click.option(
    '--hexfile',
    type=click.Path(exists=True),
    help='Hexfile to flash.')
def flash(ctx, dut, mcu, hexfile):
    if dut is None:
        dut = get_default_gateway(ctx)
    session = ctx.obj.session
    files = [
        ('hexfile', open(hexfile, 'rb').read()),
    ]
    if mcu:
        files.append(('mcu', mcu))

    out = session.debug_flash(dut, files).json()
    print(out['output'])
    click.secho('Flashed!', fg='green')


@_debug.command()
@click.pass_context
@click.option('--dut', required=False, help='ID of DUT')
@click.option('--mcu', required=False, help='MCU to disconnect')
@click.option('--halt', is_flag=True, help='Halt the DUT after reset. Default: do not halt', default=False, show_default=True)
def reset(ctx, dut, mcu, halt):
    if dut is None:
        dut = get_default_gateway(ctx)
    session = ctx.obj.session

    session.debug_reset(dut, mcu, halt).json()
    if halt:
        click.secho('Device reset & halted;', fg='green')
    else:
        click.secho('Device reset; not halted;', fg='green')
