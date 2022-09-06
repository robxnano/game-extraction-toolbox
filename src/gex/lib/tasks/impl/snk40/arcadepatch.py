import logging
from gex.lib.tasks import helpers
from gex.lib.utils.blob import transforms

logger = logging.getLogger('gextoolbox')

out_file_info = [
    {
        "game": "Chopper I",
        "system": "Arcade",
        "filename": "chopperb.zip",
        "notes": []
    },
    {
        "game": "Chopper I",
        "system": "Arcade",
        "filename": "legofair.zip",
        "notes": [3]
    },
    {
        "game": "Fantasy",
        "system": "Arcade",
        "filename": "fantasyj.zip",
        "notes": []
    },
    {
        "game": "Fantasy",
        "system": "Arcade",
        "filename": "fantasyu.zip",
        "notes": []
    },
    {
        "game": "Time Soldiers",
        "system": "Arcade",
        "filename": "btlfield.zip",
        "notes": [3]
    },
    {
        "game": "Time Soldiers",
        "system": "Arcade",
        "filename": "timesold.zip",
        "notes": [3]
    },
    {
        "game": "Munch Mobile (Joyful Road)",
        "system": "Arcade",
        "filename": "mnchmobl.zip",
        "notes": []
    },
    {
        "game": "Munch Mobile (Joyful Road)",
        "system": "Arcade",
        "filename": "ASO_jp.zip",
        "notes": []
    },
    {
        "game": "Sasuke vs. Commander",
        "system": "Arcade",
        "filename": "sasuke.zip",
        "notes": []
    },
    {
        "game": "Ozma Wars",
        "system": "Arcade",
        "filename": "ozmawars.zip",
        "notes": [2]
    },
    {
        "game": "Paddle Mania",
        "system": "Arcade",
        "filename": "paddlema.zip",
        "notes": [2]
    }
]

def extract(bundle_contents):
    out_files = []
    contents = bundle_contents['patch']
    out_files.extend(_handle_chopper(contents))
    out_files.extend(_handle_fantasy(contents))
    out_files.extend(_handle_timesoldiers(contents))
    out_files.extend(_handle_munchmobile(contents))
    out_files.extend(_handle_sasuke(contents))
    out_files.extend(_handle_ozmawars(contents))
    out_files.extend(_handle_paddlemania(contents))
    return out_files

def _handle_chopper(mbundle_entries):
    out_files = []

    # CHOPPERB
    func_map = {}
    func_map['maincpu'] = helpers.name_file_helper("chopper.maincpu", "kk1.8g")
    func_map['sub'] = helpers.name_file_helper("chopper.sub", "kk4.6g")
    prom_file_names = [
        "1.9w",
        "3.9u",
        "2.9v"
    ]
    func_map['prom'] = helpers.equal_split_helper("chopper.proms", prom_file_names)
    func_map['audiocpu'] = helpers.name_file_helper("chopper.audiocpu", "kk3.3d")
    func_map['tx'] = helpers.name_file_helper("chopper.tx_tiles", "kk5.8p")
    bg_file_names = [
        "kk10.8y",
        "kk11.8z",
        "kk12.8ab",
        "kk13.8ac"
    ]
    func_map['bg'] = helpers.equal_split_helper("chopper.bg_tiles", bg_file_names)
    sp16_file_names = [
        "kk9.3k",
        "kk8.3l",
        "kk7.3n",
        "kk6.3p"
    ]
    func_map['sp16'] = helpers.equal_split_helper("chopper.sp16_tiles", sp16_file_names)
    sp32_file_names = [
        "kk18.3ab",
        "kk19.2ad",
        "kk20.3y",
        "kk21.3aa",
        "kk14.3v",
        "kk15.3x",
        "kk16.3s",
        "kk17.3t"
    ]
    func_map['sp32'] = helpers.equal_split_helper("chopper.sp32_tiles", sp32_file_names)
    func_map['ym2'] = helpers.name_file_helper("chopper.ym2", "kk2.3j")
    func_map['plds'] = helpers.name_file_helper("chopper.plds", "p-a1.2c")
    mame_name = "chopperb.zip"
    logger.info(f"Building {mame_name}...")
    out_files.append(
        {'filename': mame_name, 'contents': helpers.build_rom(mbundle_entries, func_map)}
    )
    logger.info(f"Extracted {mame_name}.")

    # LEGOFAIR
    func_map = {}
    func_map['maincpu'] = helpers.name_file_helper("legofair.maincpu", "kk1.4m")
    func_map['sub'] = helpers.name_file_helper("legofair.sub", "kk4.8m")
    prom_file_names = [
        "1.1k",
        "2.1l",
        "3.2k"
    ]
    func_map['prom'] = helpers.equal_split_helper("chopper.proms", prom_file_names)
    func_map['audiocpu'] = helpers.name_file_helper("chopper.audiocpu", "kk3.6j")
    func_map['tx'] = helpers.name_file_helper("chopper.tx_tiles", "kk5.3a")
    bg_file_names = [
        "kk10.1a",
        "kk11.1b",
        "kk12.1d",
        "kk13.1e"
    ]
    func_map['bg'] = helpers.equal_split_helper("chopper.bg_tiles", bg_file_names)
    sp16_file_names = [
        "kk9.3g",
        "kk8.3e",
        "kk7.3d",
        "kk6.3b"
    ]
    func_map['sp16'] = helpers.equal_split_helper("chopper.sp16_tiles", sp16_file_names)
    sp32_file_names = [
        "kk18.8m",
        "kk19.8n",
        "kk20.8p",
        "kk21.8s",
        "kk14.7p",
        "kk15.7s",
        "kk16.8j",
        "kk17.8k"
    ]
    func_map['sp32'] = helpers.equal_split_helper("chopper.sp32_tiles", sp32_file_names)
    func_map['ym2'] = helpers.name_file_helper("chopper.ym2", "kk2.5b")
    func_map['plds'] = helpers.name_file_helper("chopper.plds", "p-a1.8b")
    mame_name = "legofair.zip"
    logger.info(f"Building {mame_name}...")
    out_files.append(
        {'filename': mame_name, 'contents': helpers.build_rom(mbundle_entries, func_map)}
    )
    logger.info(f"Extracted {mame_name}.")

    return out_files

def _handle_fantasy(mbundle_entries):
    out_files = []
    # COMMON
    func_map = {}
    gfx1_file_names = [
        "fs10ic50.bin",
        "fs11ic51.bin"
    ]
    func_map['gfx1'] = helpers.equal_split_helper("fantasyu.gfx1", gfx1_file_names)
    snk6502_file_names = [
        "fs_b_51.bin",
        "fs_a_52.bin",
        "fs_c_53.bin"
    ]
    func_map['snk6502'] = helpers.equal_split_helper("fantasyu.snk6502", snk6502_file_names)
    speech_file_names = [
        "fs_d_7.bin",
        "fs_e_8.bin",
        "fs_f_11.bin"
    ]
    func_map['speech'] = helpers.equal_split_helper("fantasyu.speech", speech_file_names)
    logger.info("Processing fantasy common files...")
    common_file_map = helpers.process_rom_files(mbundle_entries, func_map)

    # FANTASYJ
    func_map = {}
    prom_file_names = [
        "prom-8.bpr",
        "prom-7.bpr"
    ]
    func_map['prom'] = helpers.equal_split_helper("fantasyj.proms", prom_file_names)
    maincpu_file_names = [
        "fs5jic12.bin",
        "fs1jic7.bin",
        "fs2jic8.bin",
        "fs3jic9.bin",
        "fs4jic10.bin",
        "fs6jic14.bin",
        "fs7jic15.bin",
        "fs8jic16.bin",
        "fs9jic17.bin"
    ]
    func_map['maincpu'] = helpers.equal_split_helper("fantasyj.maincpu", maincpu_file_names)
    func_map['common'] = helpers.existing_files_helper(common_file_map)
    mame_name = "fantasyj.zip"
    logger.info(f"Building {mame_name}...")
    out_files.append(
        {'filename': mame_name, 'contents': helpers.build_rom(mbundle_entries, func_map)}
    )
    logger.info(f"Extracted {mame_name}.")

    # FANTASYU
    func_map = {}
    prom_file_names = [
        "fantasy.ic7",
        "fantasy.ic6"
    ]
    func_map['prom'] = helpers.equal_split_helper("fantasyu.proms", prom_file_names)
    maincpu_file_names = [
        "ic12.cpu",
        "ic07.cpu",
        "ic08.cpu",
        "ic09.cpu",
        "ic10.cpu",
        "ic14.cpu",
        "ic15.cpu",
        "ic16.cpu",
        "ic17.cpu"
    ]
    func_map['maincpu'] = helpers.equal_split_helper("fantasyu.maincpu", maincpu_file_names)

    func_map['common'] = helpers.existing_files_helper(common_file_map)
    mame_name = "fantasyu.zip"
    logger.info(f"Building {mame_name}...")
    out_files.append(
        {'filename': mame_name, 'contents': helpers.build_rom(mbundle_entries, func_map)}
    )
    logger.info(f"Extracted {mame_name}.")

    return out_files

def _handle_timesoldiers(mbundle_entries):
    out_files = []

    # Common
    func_map = {}
    z80_file_names = [
        "bf.7",
        "bf.8",
        "bf.9"
    ]
    func_map['z80'] = helpers.equal_split_helper("TimeSoldiers.z80", z80_file_names)
    gfx2_file_names = [
        "bf.10",
        "bf.14",
        "bf.18",
        "bf.11",
        "bf.15",
        "bf.19",
        "bf.12",
        "bf.16",
        "bf.20",
        "bf.13",
        "bf.17",
        "bf.21"
    ]
    def timesold_gfx2(in_file_name, filenames):
        def process(in_files):
            contents = in_files[in_file_name]
            contents = transforms.splice_out(contents, start=15*131072, length=131072)
            contents = transforms.splice_out(contents, start=11*131072, length=131072)
            contents = transforms.splice_out(contents, start=7*131072, length=131072)
            contents = transforms.splice_out(contents, start=3*131072, length=131072)
            chunks = transforms.equal_split(contents, len(filenames))
            return dict(zip(filenames, chunks))
        return process
    func_map['gfx2'] = timesold_gfx2("TimeSoldiers.gfx2.rom", gfx2_file_names)

    logger.info("Processing timesold common files...")
    common_file_map = helpers.process_rom_files(mbundle_entries, func_map)


    def timesold_maincpu_common(in_file_name, filenames):
        def maincpu(in_files):
            contents = in_files[in_file_name]
            chunks = transforms.equal_split(contents, 2)
            chunks = transforms.deinterleave_all(chunks, num_ways=2, word_size=1)
            return dict(zip(filenames, chunks))
        return maincpu

    # TIMESOLD
    func_map = {}
    maincpu_file_names = [
        "bf.3",
        "bf.4",
        "bf.1",
        "bf.2"
    ]
    func_map['maincpu'] = timesold_maincpu_common("TimeSoldiers.3.68k", maincpu_file_names)
    gfx1_file_names = [
        "bf.6",
        "bf.5"
    ]
    func_map['gfx1'] = helpers.deinterleave_helper("TimeSoldiers.u.gfx1.rom",
        gfx1_file_names, num_ways=2, word_size=1)
    func_map['common'] = helpers.existing_files_helper(common_file_map)

    mame_name = "timesold.zip"
    logger.info(f"Building {mame_name}...")
    out_files.append(
        {'filename': mame_name, 'contents': helpers.build_rom(mbundle_entries, func_map)}
    )
    logger.info(f"Extracted {mame_name}.")

    # BTLFIELD
    func_map = {}
    maincpu_file_names = [
        "bfv1_03.bin",
        "bfv1_04.bin",
        "bf.1",
        "bf.2"
    ]
    func_map['maincpu'] = timesold_maincpu_common("TimeSoldiers.j.68k", maincpu_file_names)
    gfx1_file_names = [
        "bfv1_06.bin",
        "bfv1_05.bin"
    ]
    func_map['gfx1'] = helpers.deinterleave_helper("TimeSoldiers.j.gfx1.rom",
        gfx1_file_names, num_ways=2, word_size=1)
    func_map['common'] = helpers.existing_files_helper(common_file_map)

    mame_name = "btlfield.zip"
    logger.info(f"Building {mame_name}...")
    out_files.append(
        {'filename': mame_name, 'contents': helpers.build_rom(mbundle_entries, func_map)}
    )
    logger.info(f"Extracted {mame_name}.")

    return out_files

def _handle_munchmobile(mbundle_entries):
    out_files = []

    # Common
    func_map = {}
    func_map['audiocpu'] = helpers.name_file_helper("joyfulr.audiocpu", "mu.2j")
    func_map['proms'] = helpers.name_file_helper("joyfulr.proms", "a2001.clr")
    gfx1_file_names = [
        "s1.10a",
        "s2.10b"
    ]
    func_map['gfx1'] = helpers.equal_split_helper("joyfulr.gfx1", gfx1_file_names)
    gfx2_file_names = [
        "b1.2c",
        "b2.2b"
    ]
    func_map['gfx2'] = helpers.equal_split_helper("joyfulr.gfx2", gfx2_file_names)
    func_map['gfx4'] = helpers.name_file_helper("joyfulr.gfx4", "h")

    logger.info("Processing joyfulr common files...")
    common_file_map = helpers.process_rom_files(mbundle_entries, func_map)

    # JOYFULR
    func_map = {}
    maincpu_file_names = [
        "m1j.10e",
        "m2j.10d"
    ]
    func_map['maincpu'] = helpers.equal_split_helper("joyfulr.maincpu", maincpu_file_names)
    gfx3_file_names = [
        "f1j.1g",
        "f2j.3g",
        "f3j.5g"
    ]
    func_map['gfx3'] = helpers.equal_split_helper("joyfulr.gfx3", gfx3_file_names)
    func_map['common'] = helpers.existing_files_helper(common_file_map)
    mame_name = "joyfulr.zip"
    logger.info(f"Building {mame_name}...")
    out_files.append(
        {'filename': mame_name, 'contents': helpers.build_rom(mbundle_entries, func_map)}
    )
    logger.info(f"Extracted {mame_name}.")

    # MNCHMOBL
    func_map = {}
    maincpu_file_names = [
        "m1.10e",
        "m2.10d"
    ]
    func_map['maincpu'] = helpers.equal_split_helper("mnchmobl.maincpu", maincpu_file_names)
    gfx3_file_names = [
        "f1.1g",
        "f2.3g",
        "f3.5g"
    ]
    func_map['gfx3'] = helpers.equal_split_helper("mnchmobl.gfx3", gfx3_file_names)
    func_map['common'] = helpers.existing_files_helper(common_file_map)
    mame_name = "mnchmobl.zip"
    logger.info(f"Building {mame_name}...")
    out_files.append(
        {'filename': mame_name, 'contents': helpers.build_rom(mbundle_entries, func_map)}
    )
    logger.info(f"Extracted {mame_name}.")

    return out_files

def _handle_sasuke(mbundle_entries):
    out_files = []

    func_map = {}
    maincpu_file_names = [
        "sc1",
        "sc2",
        "sc3",
        "sc4",
        "sc5",
        "sc6",
        "sc7",
        "sc8",
        "sc9",
        "sc10"
    ]
    func_map['maincpu'] = helpers.equal_split_helper('sasuke.maincpu', maincpu_file_names)
    gfx1_file_names = [
        "mcs_c",
        "mcs_d"
    ]
    func_map['gfx1'] = helpers.equal_split_helper('sasuke.gfx1', gfx1_file_names)
    func_map['proms'] = helpers.name_file_helper("sasuke.proms", "sasuke.clr")
    func_map['snk6502'] = helpers.name_file_helper("sasuke.snk6502", "sc11")

    mame_name = "sasuke.zip"
    logger.info(f"Building {mame_name}...")
    out_files.append(
        {'filename': mame_name, 'contents': helpers.build_rom(mbundle_entries, func_map)}
    )
    logger.info(f"Extracted {mame_name}.")

    return out_files

def _handle_ozmawars(mbundle_entries):
    out_files = []

    func_map = {}
    maincpu_file_names = [
        "mw01",
        "mw02",
        "mw03",
        "mw04",
        "mw05",
        "mw06"
    ]
    def ozmawars_maincpu(in_file_name, filenames):
        def maincpu(in_files):
            contents = in_files[in_file_name]
            contents = transforms.splice_out(contents, start = 8192, end = 16384)
            chunks = transforms.equal_split(contents, len(filenames))
            return dict(zip(filenames, chunks))
        return maincpu
    func_map['gfx2'] = ozmawars_maincpu("ozmawars.maincpu", maincpu_file_names)
    prom_file_names = [
        "01.1",
        "02.2"
    ]
    func_map['prom'] = helpers.equal_split_helper('moonbase.proms', prom_file_names)
    mame_name = "ozmawars.zip"
    logger.info(f"Building {mame_name}...")
    out_files.append(
        {'filename': mame_name, 'contents': helpers.build_rom(mbundle_entries, func_map)}
    )
    logger.info(f"Extracted {mame_name}.")

    return out_files

def _handle_paddlemania(mbundle_entries):
    func_map = {}

    prom_file_map = {
        "padlem.a": 0x100,
        "padlem.b": 0x100,
        "padlem.c": 0x100,
        "padlem.17j": 0x400,
        "padlem.16j": 0x400
    }
    func_map['prom'] = helpers.custom_split_helper('PaddleMania.proms.rom', prom_file_map)
    func_map['audiocpu'] = helpers.name_file_helper('PaddleMania.z80', 'padlem.18c')
    func_map['color_prom'] = helpers.name_file_helper('PaddleMania.clut.rom', 'padlem.18n')
    maincpu_file_names = [
        "padlem.6g",
        "padlem.3g",
        "padlem.6h",
        "padlem.3h"
    ]
    def padlem_maincpu(in_file_name, filenames):
        def maincpu(in_files):
            contents = in_files[in_file_name]
            chunks = transforms.equal_split(contents, len(filenames) // 2)
            chunks = transforms.deinterleave_all(chunks, num_ways=2, word_size=1)
            return dict(zip(filenames, chunks))
        return maincpu
    func_map['maincpu'] = padlem_maincpu('PaddleMania.1.68k', maincpu_file_names)
    gfx1_file_names = [
        "padlem.9m",
        "padlem.16m",
        "padlem.9n",
        "padlem.16n",
        "padlem.6m",
        "padlem.13m",
        "padlem.6n",
        "padlem.13n"
    ]
    func_map['gfx1'] = padlem_maincpu('PaddleMania.gfx1.rom', gfx1_file_names)
    mame_name = "paddlema.zip"
    logger.info(f"Building {mame_name}...")
    out_files = []
    out_files.append(
        {'filename': mame_name, 'contents': helpers.build_rom(mbundle_entries, func_map)}
    )
    logger.info(f"Extracted {mame_name}.")

    return out_files