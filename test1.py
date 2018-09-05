#!/usr/bin/env python3
"""Load an audio file into memory and play its contents.
NumPy and the soundfile module (http://PySoundFile.rtfd.io/) must be
installed for this to work.
This example program loads the whole file into memory before starting
playback.
To play very long files, you should use play_long_file.py instead.
"""
import argparse
import sounddevice as sd
import soundfile as sf
# import wx
#
# app = wx.App()
# frm = wx.Frame(None, title="Hello World")
# frm.Show()
# app.MainLoop()


def play(args):
    try:
        data, fs = sf.read(args.filename, dtype='float32')
        sd.play(data, fs, device=args.device)
        status = sd.wait()
        if status:
            parser.exit('Error during playback: ' + str(status))
    except KeyboardInterrupt:
        parser.exit('\nInterrupted by user')
    except Exception as e:
        parser.exit(type(e).__name__ + ': ' + str(e))


def list(args):
    print(vars(args))

    print(sd.query_devices())
    parser.exit()



def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

# create the top-level parser
parser = argparse.ArgumentParser(prog='test1.py')
subparsers = parser.add_subparsers(help='sub-command help')

# create the parser for the "play" command
parser_play = subparsers.add_parser('play', help='play a soundfile')
parser_play.add_argument('-d', '--device', type=int_or_str,
                    help='output device (numeric ID or substring)')
parser_play.add_argument('filename', help='play a sound')
parser_play.set_defaults(func=play)

# create the parser for the "list" command
parser_list = subparsers.add_parser('list', help='list the available sound devices')
parser_list.set_defaults(func=list)
# parser_b.add_argument('--baz', choices='XYZ', help='baz help')

# parse some argument lists
args = parser.parse_args()
args.func(args)
