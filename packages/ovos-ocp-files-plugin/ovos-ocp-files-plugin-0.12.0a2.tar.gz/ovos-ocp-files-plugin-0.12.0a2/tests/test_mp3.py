import struct

from ward import (
	each,
	raises,
	test,
	using,
)

from ovos_ocp_files_plugin import (
	FormatError,
	LAMEBitrateMode,
	LAMEChannelMode,
	LAMEEncodingFlags,
	LAMEHeader,
	LAMEPreset,
	LAMEReplayGain,
	LAMEReplayGainOrigin,
	LAMEReplayGainType,
	LAMESurroundInfo,
	MP3ChannelMode,
	MP3StreamInfo,
	MPEGFrameHeader,
	VBRIHeader,
	VBRIToC,
	XingHeader,
	XingToC,
)
from tests.fixtures import (
	flac_vorbis,
	lame_header,
	lame_replay_gain,
	lame_replay_gain_negative,
	lame_replay_gain_null,
	mp3_cbr_2_frames,
	mp3_lame_vbr,
	mp3_sync_branch,
	mpeg_frame,
	null,
	vbri_header,
	xing_header_no_lame,
	xing_toc,
)
from tests.utils import strip_repr


@test(
	"LAMEReplayGain",
	tags=['unit', 'mp3', 'lame', 'LAMEReplayGain'],
)
@using(
	lame_replay_gain=lame_replay_gain,
	lame_replay_gain_null=lame_replay_gain_null,
	lame_replay_gain_negative=lame_replay_gain_negative,
)
def _(
	lame_replay_gain,
	lame_replay_gain_null,
	lame_replay_gain_negative,
):
	replay_gain_parse = LAMEReplayGain.parse(lame_replay_gain)
	replay_gain_init = LAMEReplayGain(
		peak=0.21856749057769775,
		track_type=1,
		track_origin=3,
		track_adjustment=6.8,
		album_type=0,
		album_origin=0,
		album_adjustment=0.0
	)

	assert replay_gain_parse == replay_gain_init
	assert replay_gain_parse.peak == replay_gain_init.peak == 0.21856749057769775
	assert replay_gain_parse.track_type == replay_gain_init.track_type == 1
	assert replay_gain_parse.track_origin == replay_gain_init.track_origin == 3
	assert replay_gain_parse.track_adjustment == replay_gain_init.track_adjustment == 6.8
	assert replay_gain_parse.album_type == replay_gain_init.album_type == 0
	assert replay_gain_parse.album_origin == replay_gain_init.album_origin == 0
	assert replay_gain_parse.album_adjustment == replay_gain_init.album_adjustment == 0.0

	replay_gain_parse = LAMEReplayGain.parse(lame_replay_gain_null)
	replay_gain_init = LAMEReplayGain(
		peak=None,
		track_type=0,
		track_origin=0,
		track_adjustment=0.0,
		album_type=0,
		album_origin=0,
		album_adjustment=0.0
	)

	assert replay_gain_parse == replay_gain_init
	assert replay_gain_parse.peak is replay_gain_init.peak is None
	assert replay_gain_parse.track_type == replay_gain_init.track_type == 0
	assert replay_gain_parse.track_origin == replay_gain_init.track_origin == 0
	assert replay_gain_parse.track_adjustment == replay_gain_init.track_adjustment == 0.0
	assert replay_gain_parse.album_type == replay_gain_init.album_type == 0
	assert replay_gain_parse.album_origin == replay_gain_init.album_origin == 0
	assert replay_gain_parse.album_adjustment == replay_gain_init.album_adjustment == 0.0

	replay_gain_parse = LAMEReplayGain.parse(lame_replay_gain_negative)
	replay_gain_init = LAMEReplayGain(
		peak=0.21856749057769775,
		track_type=1,
		track_origin=3,
		track_adjustment=-6.8,
		album_type=0,
		album_origin=0,
		album_adjustment=-0.0
	)

	assert replay_gain_parse == replay_gain_init
	assert replay_gain_parse.peak == replay_gain_init.peak == 0.21856749057769775
	assert replay_gain_parse.track_type == replay_gain_init.track_type == 1
	assert replay_gain_parse.track_origin == replay_gain_init.track_origin == 3
	assert replay_gain_parse.track_adjustment == replay_gain_init.track_adjustment == -6.8
	assert replay_gain_parse.album_type == replay_gain_init.album_type == 0
	assert replay_gain_parse.album_origin == replay_gain_init.album_origin == 0
	assert replay_gain_parse.album_adjustment == replay_gain_init.album_adjustment == -0.0


@test(
	"LAMEEncodingFlags",
	tags=['unit', 'mp3', 'lame', 'LAMEEncodingFlags'],
)
def _(
	flags=each(
		LAMEEncodingFlags(
			nogap_continuation=1,
			nogap_continued=1,
			nspsytune=1,
			nssafejoint=1,
		),
		LAMEEncodingFlags(
			nogap_continuation=True,
			nogap_continued=True,
			nspsytune=True,
			nssafejoint=True,
		),
		LAMEEncodingFlags(
			nogap_continuation=0,
			nogap_continued=0,
			nspsytune=0,
			nssafejoint=0,
		),
		LAMEEncodingFlags(
			nogap_continuation=False,
			nogap_continued=False,
			nspsytune=False,
			nssafejoint=False,
		),
	),
	expected=each(
		True,
		True,
		False,
		False,
	)
):
	assert all(
		flag is expected
		for flag in flags.values()
	)


@test(
	"LAMEHeader",
	tags=['unit', 'mp3', 'lame', 'LAMEHeader']
)
@using(
	null=null,
	lame_header=lame_header,
)
def _(null, lame_header):
	with raises(FormatError) as exc:
		LAMEHeader.parse(null, 100)
	assert str(exc.raised) == "Valid LAME header not found."

	lame_header_parse = LAMEHeader.parse(lame_header, 100)
	lame_header_init = LAMEHeader(
		crc=b'\x1d|',
		ath_type=5,
		audio_crc=b':\xe9',
		audio_size=20489,
		bitrate=32000,
		bitrate_mode=LAMEBitrateMode.VBR_METHOD_2,
		channel_mode=LAMEChannelMode.JOINT_STEREO,
		delay=576,
		encoding_flags=LAMEEncodingFlags(
			nogap_continuation=False,
			nogap_continued=False,
			nspsytune=True,
			nssafejoint=True,
		),
		lowpass_filter=22100,
		mp3_gain=0,
		noise_shaping=1,
		padding=1260,
		preset=LAMEPreset.V0,
		replay_gain=LAMEReplayGain(
			album_adjustment=0.0,
			album_origin=LAMEReplayGainOrigin.NOT_SET,
			album_type=LAMEReplayGainType.NOT_SET,
			peak=None,
			track_adjustment=0.0,
			track_origin=LAMEReplayGainOrigin.NOT_SET,
			track_type=LAMEReplayGainType.NOT_SET,
		),
		revision=0,
		source_sample_rate=1,
		surround_info=LAMESurroundInfo.NO_SURROUND,
		unwise_settings_used=False,
		version=(3, 99),
	)

	assert lame_header_parse == lame_header_init
	assert lame_header_parse._crc == lame_header_init._crc == b'\x1d|'
	assert lame_header_parse.ath_type == lame_header_init.ath_type == 5
	assert lame_header_parse.audio_crc == lame_header_init.audio_crc == b':\xe9'
	assert lame_header_parse.audio_size == lame_header_init.audio_size == 20489
	assert lame_header_parse.bitrate == lame_header_init.bitrate == 32000
	assert lame_header_parse.bitrate_mode == lame_header_init.bitrate_mode == LAMEBitrateMode.VBR_METHOD_2
	assert lame_header_parse.channel_mode == lame_header_init.channel_mode == LAMEChannelMode.JOINT_STEREO
	assert lame_header_parse.delay == lame_header_init.delay == 576
	assert lame_header_parse.encoding_flags == lame_header_init.encoding_flags == LAMEEncodingFlags(
		nogap_continuation=False,
		nogap_continued=False,
		nspsytune=True,
		nssafejoint=True,
	)
	assert lame_header_parse.lowpass_filter == lame_header_init.lowpass_filter == 22100
	assert lame_header_parse.mp3_gain == lame_header_init.mp3_gain == 0
	assert lame_header_parse.noise_shaping == lame_header_init.noise_shaping == 1
	assert lame_header_parse.padding == lame_header_init.padding == 1260
	assert lame_header_parse.preset == lame_header_init.preset == LAMEPreset.V0
	assert lame_header_parse.replay_gain == lame_header_init.replay_gain == LAMEReplayGain(
		album_adjustment=0.0,
		album_origin=LAMEReplayGainOrigin.NOT_SET,
		album_type=LAMEReplayGainType.NOT_SET,
		peak=None,
		track_adjustment=0.0,
		track_origin=LAMEReplayGainOrigin.NOT_SET,
		track_type=LAMEReplayGainType.NOT_SET,
	)
	assert lame_header_parse.revision == lame_header_init.revision == 0
	assert lame_header_parse.source_sample_rate == lame_header_init.source_sample_rate == 1
	assert lame_header_parse.surround_info == lame_header_init.surround_info == LAMESurroundInfo.NO_SURROUND
	assert lame_header_parse.unwise_settings_used is lame_header_init.unwise_settings_used is False
	assert lame_header_parse.version == lame_header_init.version == (3, 99)
	assert strip_repr(lame_header_parse) == strip_repr(lame_header_init) == (
		"<LAMEHeader({'ath_type': 5, 'audio_crc': b':\\xe9', 'audio_size': '20.01 KiB', 'bitrate': '32 Kbps', "
		"'bitrate_mode': <LAMEBitrateMode.VBR_METHOD_2>, 'channel_mode': <LAMEChannelMode.JOINT_STEREO>, 'delay': 576, "
		"'encoding_flags': <LAMEEncodingFlags({'nogap_continuation': False, 'nogap_continued': False, 'nspsytune': True, "
		"'nssafejoint': True, })>, 'lowpass_filter': 22100, 'mp3_gain': 0, 'noise_shaping': 1, 'padding': 1260, "
		"'preset': <LAMEPreset.V0>, 'replay_gain': <LAMEReplayGain({'album_adjustment': 0.0, "
		"'album_origin': <LAMEReplayGainOrigin.NOT_SET>, 'album_type': <LAMEReplayGainType.NOT_SET>, 'peak': None, "
		"'track_adjustment': 0.0, 'track_origin': <LAMEReplayGainOrigin.NOT_SET>, 'track_type': <LAMEReplayGainType.NOT_SET>, })>, "
		"'revision': 0, 'source_sample_rate': '1.0 Hz', 'surround_info': <LAMESurroundInfo.NO_SURROUND>, "
		"'unwise_settings_used': False, 'version': (3, 99),})>"
	)


@test(
	"XingHeader",
	tags=['unit', 'mp3', 'xing', 'XingHeader'],
)
@using(
	null=null,
	xing_header_no_lame=xing_header_no_lame,
)
def _(null, xing_header_no_lame):
	with raises(FormatError) as exc:
		XingHeader.parse(null)
	assert str(exc.raised) == "Valid Xing header not found."

	xing_header_parse = XingHeader.parse(xing_header_no_lame)
	xing_header_init = XingHeader(
		lame=None,
		num_bytes=20489,
		num_frames=193,
		quality=100,
		toc=XingToC(bytearray(xing_header_no_lame[16:116]))
	)

	assert xing_header_parse == xing_header_init
	assert xing_header_parse._lame is xing_header_init._lame is None
	assert xing_header_parse.num_bytes == xing_header_init.num_bytes == 20489
	assert xing_header_parse.num_frames == xing_header_init.num_frames == 193
	assert xing_header_parse.quality == xing_header_init.quality == 100
	assert xing_header_parse.toc == xing_header_init.toc == XingToC(bytearray(xing_header_no_lame[16:116]))


@test(
	"VBRIHeader",
	tags=['unit', 'mp3', 'vbri', 'VBRIHeader'],
)
@using(vbri_header=vbri_header)
def _(vbri_header):
	with raises(FormatError) as exc:
		VBRIHeader.parse(vbri_header[4:])
	assert str(exc.raised) == "Valid VBRI header not found."

	with raises(FormatError) as exc:
		VBRIHeader.parse(vbri_header[:23] + b'\x01' + vbri_header[24:])
	assert str(exc.raised) == "Invalid VBRI TOC entry size."

	toc_entries = []
	i = 26
	for _ in range(193):
		toc_entries.append(
			struct.unpack(
				'>H',
				vbri_header[i : i + 2]
			)[0]
		)
		i += 2

	vbri_header_parse = VBRIHeader.parse(vbri_header)
	vbri_header_init = VBRIHeader(
		delay=0.00015842914581298828,
		num_bytes=20594,
		num_frames=194,
		num_toc_entries=193,
		quality=75,
		toc=VBRIToC(toc_entries),
		toc_entry_num_bytes=2,
		toc_entry_num_frames=1,
		toc_scale_factor=1,
		version=1,
	)

	assert vbri_header_parse == vbri_header_init
	assert vbri_header_parse.delay == vbri_header_init.delay == 0.00015842914581298828
	assert vbri_header_parse.num_bytes == vbri_header_init.num_bytes == 20594
	assert vbri_header_parse.num_frames == vbri_header_init.num_frames == 194
	assert vbri_header_parse.num_toc_entries == vbri_header_init.num_toc_entries == 193
	assert vbri_header_parse.quality == vbri_header_init.quality == 75
	assert vbri_header_parse.toc == vbri_header_init.toc == VBRIToC(toc_entries)
	assert vbri_header_parse.toc_entry_num_bytes == vbri_header_init.toc_entry_num_bytes == 2
	assert vbri_header_parse.toc_entry_num_frames == vbri_header_init.toc_entry_num_frames == 1
	assert vbri_header_parse.toc_scale_factor == vbri_header_init.toc_scale_factor == 1
	assert vbri_header_parse.version == vbri_header_init.version == 1


@test(
	"MPEGFrameHeader",
	tags=['unit', 'mp3', 'MPEGFrameHeader'],
)
@using(
	mpeg_frame=mpeg_frame,
	xing_toc=xing_toc,
)
def _(mpeg_frame, xing_toc):
	with raises(FormatError) as exc:
		MPEGFrameHeader.parse(mpeg_frame[2:])
	assert str(exc.raised) == "Invalid MPEG frame sync."

	with raises(FormatError) as exc:
		MPEGFrameHeader.parse(mpeg_frame[0:1] + b'\xEE' + mpeg_frame[2:])
	assert str(exc.raised) == "Invalid MPEG audio frame."

	mpeg_frame_parse = MPEGFrameHeader.parse(mpeg_frame)
	mpeg_frame_init = MPEGFrameHeader(
		start=0,
		size=417,
		vbri=None,
		xing=XingHeader(
			lame=LAMEHeader(
				crc=b'\x1d|',
				ath_type=5,
				audio_crc=b':\xe9',
				audio_size=20489,
				bitrate=32000,
				bitrate_mode=LAMEBitrateMode.VBR_METHOD_2,
				channel_mode=LAMEChannelMode.JOINT_STEREO,
				delay=576,
				encoding_flags=LAMEEncodingFlags(
					nogap_continuation=False,
					nogap_continued=False,
					nspsytune=True,
					nssafejoint=True,
				),
				lowpass_filter=22100,
				mp3_gain=0,
				noise_shaping=1,
				padding=1260,
				preset=LAMEPreset.V0,
				replay_gain=LAMEReplayGain(
					album_adjustment=0.0,
					album_origin=LAMEReplayGainOrigin.NOT_SET,
					album_type=LAMEReplayGainType.NOT_SET,
					peak=None,
					track_adjustment=0.0,
					track_origin=LAMEReplayGainOrigin.NOT_SET,
					track_type=LAMEReplayGainType.NOT_SET,
				),
				revision=0,
				source_sample_rate=1,
				surround_info=LAMESurroundInfo.NO_SURROUND,
				unwise_settings_used=False,
				version=(3, 99),
			),
			num_bytes=20489,
			num_frames=193,
			quality=100,
			toc=XingToC(xing_toc),
		),
		bitrate=128000,
		channel_mode=MP3ChannelMode.JOINT_STEREO,
		channels=2,
		layer=3,
		padded=False,
		protected=False,
		sample_rate=44100,
		version=1,
	)

	assert mpeg_frame_parse == mpeg_frame_init
	assert mpeg_frame_parse._start == mpeg_frame_init._start == 0
	assert mpeg_frame_parse._size == mpeg_frame_init._size == 417
	assert mpeg_frame_parse.bitrate == mpeg_frame_init.bitrate == 128000
	assert mpeg_frame_parse.channel_mode == mpeg_frame_init.channel_mode == MP3ChannelMode.JOINT_STEREO
	assert mpeg_frame_parse.channels == mpeg_frame_init.channels == 2
	assert mpeg_frame_parse.layer == mpeg_frame_init.layer == 3
	assert mpeg_frame_parse.padded is mpeg_frame_init.padded is False
	assert mpeg_frame_parse.protected is mpeg_frame_init.protected is False
	assert mpeg_frame_parse.sample_rate == mpeg_frame_init.sample_rate == 44100
	assert mpeg_frame_parse.version == mpeg_frame_init.version == 1
	assert strip_repr(mpeg_frame_parse) == strip_repr(mpeg_frame_init) == (
		"<MPEGFrameHeader({'bitrate': '128 Kbps', 'channel_mode': <MP3ChannelMode.JOINT_STEREO>, "
		"'channels': 2, 'layer': 3, 'padded': False, 'protected': False, 'sample_rate': '44.1 KHz', 'version': 1,})>"
	)


@test(
	"MP3StreamInfo.count_mpeg_frames",
	tags=['unit', 'mp3', 'MP3StreamInfo', 'count_mpeg_frames'],
)
@using(
	mp3_lame_vbr=mp3_lame_vbr,
	mp3_cbr_2_frames=mp3_cbr_2_frames,
	mp3_sync_branch=mp3_sync_branch,
	flac_vorbis=flac_vorbis,
)
def _(
	mp3_lame_vbr,
	mp3_cbr_2_frames,
	mp3_sync_branch,
	flac_vorbis,
):
	assert MP3StreamInfo.count_mpeg_frames(mp3_lame_vbr) == 193
	assert MP3StreamInfo.count_mpeg_frames(mp3_cbr_2_frames) == 2
	assert MP3StreamInfo.count_mpeg_frames(mp3_sync_branch) == 192
	assert MP3StreamInfo.count_mpeg_frames(flac_vorbis) == 0


@test(
	"MP3StreamInfo.find_mpeg_frames",
	tags=['unit', 'mp3', 'MP3StreamInfo', 'find_mpeg_frames'],
)
@using(
	mp3_lame_vbr=mp3_lame_vbr,
	mp3_cbr_2_frames=mp3_cbr_2_frames,
	mp3_sync_branch=mp3_sync_branch,
	flac_vorbis=flac_vorbis,
)
def _(
	mp3_lame_vbr,
	mp3_cbr_2_frames,
	mp3_sync_branch,
	flac_vorbis,
):
	frames = MP3StreamInfo.find_mpeg_frames(mp3_lame_vbr)
	assert len(frames) == 1
	assert frames[0]._xing is not None

	frames = MP3StreamInfo.find_mpeg_frames(mp3_cbr_2_frames)
	assert len(frames) == 2
	assert frames[0]._xing is None

	frames = MP3StreamInfo.find_mpeg_frames(mp3_sync_branch)
	assert len(frames) == 4
	assert frames[0]._xing is None

	with raises(FormatError) as exc:
		MP3StreamInfo.find_mpeg_frames(flac_vorbis)
	assert str(exc.raised) == "No XING header and insufficient MPEG frames."
