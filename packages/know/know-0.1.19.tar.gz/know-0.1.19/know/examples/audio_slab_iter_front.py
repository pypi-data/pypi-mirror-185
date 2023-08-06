from i2.wrapper import arg_val_converter
from i2 import Sig
from functools import partial

from audiostream2py import PyAudioSourceReader, get_input_device_index
from know.base import SlabsIter, IteratorExit


def audio_slabs(
    input_device=None,
    rate=44100,
    width=2,
    channels=1,
    frames_per_buffer=44100,  # same as sample rate for 1 second intervals
    seconds_to_keep_in_stream_buffer=60,
    launch=True,
    pipeline_commands=None,
):
    """Make an app that does something with live audio and keyboard event streams.

    The app will start two independent streams:
    one for audio and another for keyboard inputs.
    Prints stream type, timestamp, and additional info about data:
    Shows input key pressed for keyboard and byte count for audio

    Press Esc key to quit.

    :param input_device: Input device (index, name, pattern...)
    :param rate: audio sample rate
    :param width: audio byte width
    :param channels: number of audio input channels
    :param frames_per_buffer: audio samples per buffer
    :param seconds_to_keep_in_stream_buffer: max size of audio buffer before data falls off
    :param launch: If True (default) will launch the app. If False, will just return the
    app object.
    :return: None
    """
    input_device_index = get_input_device_index(input_device=input_device)

    # converts seconds_to_keep_in_stream_buffer to max number of buffers of size
    # frames_per_buffer
    audio_reader = get_audio_reader(
        rate,
        width,
        channels,
        input_device_index,
        frames_per_buffer,
        seconds_to_keep_in_stream_buffer,
    )

    app = SlabsIter(
        # source the data
        audio=audio_reader,
        # _print_info=partial(print, '', end='\n\r'),  # TODO: Address no_sig_kwargs err
        # check audio and keyboard for stopping signals
        audio_reader_instance=lambda: audio_reader,  # to give access to the audio_reader
        **(pipeline_commands or {}),
    )

    if not launch:
        return app
    else:
        app()
        print(f'\nYour session is now over.\n')


def get_audio_reader(
    rate,
    width,
    channels,
    input_device_index,
    frames_per_buffer,
    seconds_to_keep_in_stream_buffer,
):
    maxlen = PyAudioSourceReader.audio_buffer_size_seconds_to_maxlen(
        buffer_size_seconds=seconds_to_keep_in_stream_buffer,
        rate=rate,
        frames_per_buffer=frames_per_buffer,
    )
    audio_reader = PyAudioSourceReader(
        rate=rate,
        width=width,
        channels=channels,
        unsigned=True,
        input_device_index=input_device_index,
        frames_per_buffer=frames_per_buffer,
    ).stream_buffer(maxlen)
    return audio_reader


print_nr = partial(print, end='\n\r')

# TODO: Generalize to a curriable alias handling function? It's a if_cond_val pattern.
def none_if_none_string(x):
    if isinstance(x, str) and x == 'None':
        return None
    return x


def none_if_none_string_for_all_none_defaulted(func, exception_argnames=()):
    none_defaulted_args = [
        name
        for name, default in Sig(func).defaults.items()
        if default == None and name not in exception_argnames
    ]
    if none_defaulted_args:
        return arg_val_converter(
            func, **{name: none_if_none_string for name in none_defaulted_args}
        )
    return func


from know.examples.keyboard_and_audio import (
    stop_if_audio_not_running,
    IteratorExit,
    audio_to_wf,
    print_samples,
    only_if,
)

pipeline_commands = dict(
    _audio_stop=stop_if_audio_not_running,
    # _keyboard_stop=keyboard_stop,
    # handle signals
    handle_exceptions=(IteratorExit, KeyboardInterrupt),
    # do stuff
    # audio_print=audio_print,
    # keyboard_print=keyboard_print,
    # bar_char=LastCharPressed(),
    wf=audio_to_wf,
    # __1=wf_to_print,
    __2=print_samples,
    _12=lambda wf: print_nr(sum(map(abs, wf or []))),
)

# config
if __name__ == '__main__':
    from streamlitfront import mk_app

    audio_slabs(pipeline_commands=pipeline_commands)

    # w_audio_slabs = none_if_none_string_for_all_none_defaulted(w_audio_slabs)
    #
    # app = mk_app([w_audio_slabs])
    # app()
