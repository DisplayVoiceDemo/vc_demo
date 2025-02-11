from temple import one_audio_block_temple, table_temple, experiment_temple, page_temple, one_table_line
import os
import glob
abstract = """
    Voice conversion (VC) transforms source speech into a target voice by preserving the content while replacing the timbre of the source speaker with that of the target speaker. However, timbre information from the source speaker is inherently embedded in the content representations, causing significant timbre leakage and reducing similarity to the target speaker. To address this, we introduce a Universal Semantic Matching (USM) residual block to a content extractor. The residual block consists of two branches with tunable weights. One is a skip connection to the original content layer, the other is a universal semantic dictionary based Content Feature Re-expression (CFR) module. Specifically, each dictionary entry in the universal semantic dictionary represents a phoneme class, computed statistically using speech from multiple speakers, creating a stable, speaker-independent semantic set. Additionally, we introduce CFR within the USM block to obtain timbre-free and contextual content representations by expressing each content frame as a weighted linear combination of dictionary entries using corresponding phoneme posteriors as weights. Extensive experiments across various VC frameworks demonstrate that our approach effectively mitigates timbre leakage and significantly improves similarity to the target speaker.
                        """
def one_audio_block(path,name=None):
    if not name:
        name=  ""
    name = name + "<br>"
    return one_audio_block_temple.format(name=name,path=path)+ "                                <br>"

def many_audio_block(info,height:int=10000,add_td=False):
    """
        info: [(name,path),(name,path)...]
    """
    l = len(info)
    audios = ""
    info_list = []
    # 把info每height个分为一组,放到info_list中
    for i in range(0,l,height):
        info_list.append(info[i:i+height])
    for info in info_list:
        per_audios = ""   
        for per_info in info:
            name,path = per_info
            per_audios += one_audio_block(path,name)
        audios += f"<td>{per_audios}\n                                </td>"
    if add_td:
        td = "<td>{audios}\n                                  </td>"
        return td.format(audios=audios)
    else:
        return audios
    
def one_table_block(src_info,ref_info,conversion_info,tag):
    """
        一个table，如LM Model实验的F2M table,
        src_info,ref_info,conversion_info: [[(name,path),(name,path)...]]
    """
    lines = ""
    for src_name,tar_name,conversion_name in zip(src_info,ref_info,conversion_info):
        lines += one_table_line.format(
            src_audio=many_audio_block(src_name),
            tar_audio=many_audio_block(tar_name),
            conversion_audio=many_audio_block(conversion_name,height=3)
        )
    block = table_temple.format(
        lines=lines,
        test_tag=tag
    )
    return block

# def one_experiment_block(src_info_list,ref_info_list,conversion_info_list,tag_list,experiment_tag):
#     """
#         一个实验，如LM Model实验
#         src_info_list,ref_info_list,conversion_info_list: [[[(name,path),(name,path)...]]]
#     """
#     ret = ""
#     for i in range(len(src_info_list)):
#         ret += one_table_block(
#             src_info_list[i],
#             ref_info_list[i],
#             conversion_info_list[i],
#             tag_list[i]
#         )
#     return experiment_temple.format(
#         experiment_name=experiment_tag,
#         tables=ret
#     )

def put_into_page(experiment_html,title,big_header,sub_header,abstract,html_path):
    html = page_temple.format(
        title =title,
        big_header=big_header,
        sub_header=sub_header,
        abstract=abstract,
        experimental_results=experiment_html
    )
    with open(html_path,'w') as f:
        f.write(html)
    return html_path

# def generate_page(src_info_list_list,ref_info_list_list,conversion_info_list_list,tag_list_list,experiment_tag_list,html_path):
#     """
#         src_info_list_list: [[[(name,path),(name,path)...],...],...],
#                             其中src_info_list_list[0]代表第一个实验的src_info_list,
#                             src_info_list_list[0][0]代表第一个实验中第一个表格的src_info,
#                             src_info_list_list[0][0]为一个list，里面是若干个(name,path)的元组
            
#     """
def generate_exper(folder_dir,model_name_list,experiment_name):
    subfolder_to_tag = {
        "M2F": "Male-to-Female",
        "F2M": "Female-to-Male"
    }
    exper_html = ""
    for k,v in subfolder_to_tag.items():
        subfolder_dir = os.path.join(folder_dir,k)
        find_src_wavs = os.listdir(os.path.join(subfolder_dir,"src"))
        find_src_wavs = [os.path.join(subfolder_dir,"src",wav_path) for wav_path in find_src_wavs]
        find_src_wavs.sort()
        src_wavs = [[(None,wav_path)] for wav_path in find_src_wavs]
        ref_wavs = [[(None,wav_path.replace("src","ref"))] for wav_path in find_src_wavs]
        cov_wavs =  [[(name,wav_path.replace("src",str(idx))) for idx,name in enumerate(model_name_list)] for wav_path in find_src_wavs]
        exper_html += one_table_block(
            src_info=src_wavs,
            ref_info=ref_wavs,
            conversion_info=cov_wavs,
            tag = v
        )
    exper_html = experiment_temple.format(
        experiment_name=experiment_name,
        tables = exper_html
        )
    return exper_html

def generate_exper2(folder_dir,model_name_list,experiment_name):
    subfolder_to_tag = {
        "M2F": "Male-to-Female",
        "F2M": "Female-to-Male"
    }
    exper_html = ""
    src_wavs = []
    ref_wavs = []
    cov_wavs = []
    for k,v in subfolder_to_tag.items():
        subfolder_dir = os.path.join(folder_dir,k)
        find_src_wavs = os.listdir(os.path.join(subfolder_dir,"src"))
        find_src_wavs = [os.path.join(subfolder_dir,"src",wav_path) for wav_path in find_src_wavs]
        find_src_wavs.sort()
        src_wavs += [[(None,wav_path)] for wav_path in find_src_wavs]
        ref_wavs += [[(None,wav_path.replace("src","ref"))] for wav_path in find_src_wavs]
        cov_wavs +=  [[(name,wav_path.replace("src",str(idx))) for idx,name in enumerate(model_name_list)] for wav_path in find_src_wavs]
    exper_html += one_table_block(
        src_info=src_wavs,
        ref_info=ref_wavs,
        conversion_info=cov_wavs,
        tag = "PPG"
    )
    exper_html = experiment_temple.format(
        experiment_name=experiment_name,
        tables = exper_html
        )
    return exper_html

# 在指定文件的同一文件夹下寻找以指定后缀结尾的文件
def find_wav(path, suffix):
    folder_dir = os.path.dirname(path)
    find_wavs = os.listdir(folder_dir)
    find_wavs = [os.path.join(folder_dir,wav_path) for wav_path in find_wavs]
    find_wavs = [wav_path for wav_path in find_wavs if wav_path.endswith(suffix)]
    assert len(find_wavs) == 1
    return find_wavs[0]
def generate_exper3(folder_dirs,model_name_mapper,experiment_name):

    exper_html = ""
    for folder_dir in folder_dirs:
        find_src_wavs = glob.glob(os.path.join(folder_dir, '**', '*source.wav'), recursive=True)
        find_src_wavs.sort()
        src_wavs = [[(None,wav_path)] for wav_path in find_src_wavs]
        ref_wavs = [[(None,find_wav(wav_path,"prompt.wav"))] for wav_path in find_src_wavs]
        cov_wavs =  [[("MLF" if folder_dir.endswith("_hubert") and name == "BNF" else name  ,wav_path.replace("_source",path_name)) for path_name,name in model_name_mapper] for wav_path in find_src_wavs]
        
        exper_html += one_table_block(
            src_info=src_wavs,
            ref_info=ref_wavs,
            conversion_info=cov_wavs,
            tag = "PPG" if folder_dir.endswith("_ppg") else "HuBERT"
        )
    exper_html = experiment_temple.format(
        experiment_name=experiment_name,
        tables = exper_html
        )
    return exper_html



def generate_exper4(folder_dir,experiment_name,chosen_files=None,tag="PPG",mapper=None):
    exper_html = ""
    src_wavs = []
    ref_wavs = []
    cov_wavs = []
    
    subfolder_dir = folder_dir
    find_src_wavs = os.listdir(os.path.join(subfolder_dir,"src"))
    find_src_wavs = [os.path.join(subfolder_dir,"src",wav_path) for wav_path in find_src_wavs]
    if chosen_files is not None:
        find_src_wavs = [wav_path for wav_path in find_src_wavs if os.path.basename(wav_path) in chosen_files]
    find_src_wavs.sort()
    src_wavs += [[(None,wav_path)] for wav_path in find_src_wavs]
    ref_wavs += [[(None,wav_path.replace("src","ref"))] for wav_path in find_src_wavs]
    find_folders = os.listdir(subfolder_dir)
    find_folders = [f for f in find_folders if f != "src" and f != "ref" and f != ".DS_Store"]
    #find_folders = [f.replace("_star","*") for f in find_folders]
    find_folders.sort()
    #cov_wavs +=  [[(name.replace("_star","*"),wav_path.replace("src",name)) for idx,name in enumerate(find_folders)] for wav_path in find_src_wavs]
    for wav_path in find_src_wavs:
        this_cov_wavs = []
        for idx,name in enumerate(find_folders) :
            new_wav_path = wav_path.replace("src",name)
            if mapper is not None:
                for old,new in mapper:
                    name = name.replace(old,new)
            this_cov_wavs.append((name,new_wav_path))
        cov_wavs.append(this_cov_wavs)
    # 递归遍历folder_dir，如果文件的文件名不在chosen_files 就删掉
    for root, dirs, files in os.walk(subfolder_dir):
        for file in files:
            if file not in chosen_files:
                os.remove(os.path.join(root, file))
                print("Delete {}".format(os.path.join(root, file)))
    exper_html += one_table_block(
        src_info=src_wavs,
        ref_info=ref_wavs,
        conversion_info=cov_wavs,
        tag = tag
    )
    exper_html = experiment_temple.format(
        experiment_name=experiment_name,
        tables = exper_html
        )
    return exper_html

if __name__ == "__main__":
    exper_html = ""
    # exper_html += generate_exper3(
    #     folder_dirs=["samples/vits_ppg","samples/vits_hubert"],
    #     model_name_mapper=[
    #         ("_base","BNF"),
    #         ("_soft","S-Unit"),
    #         ("_dict","USM")
    #     ],
    #     experiment_name = "VITS"
    # )

    # exper_html += generate_exper3(
    #     folder_dirs=["samples/lm_ppg","samples/lm_hubert"],
    #     model_name_mapper=[
    #         ("_base","BNF"),
    #         ("_soft","S-Unit"),
    #         ("_dict","USM")
    #     ],
    #     experiment_name = "LM Model"
    # )
        
    # exper_html += generate_exper2(
    #     folder_dir="samples/diffusion",
    #     model_name_list=["BNF","S-Unit","USM"],
    #     experiment_name = "Diffusion Model"
    # )
    exper_html += generate_exper4(
        folder_dir="samples/vits_hu",
        experiment_name = "VITS",
        chosen_files=['35.wav',"61.wav","96.wav"],
        tag="HuBERT",
        mapper=[
            ("base","MLF"),
            ("soft","S-Unit"),
            ("usm","USM"),
            ("_star","*")
        ],
    )
    
    exper_html += generate_exper4(
        folder_dir="samples/vits_ppg",
        experiment_name = "",
        chosen_files = ["71.wav","66.wav","62.wav"],
        tag="PPG",
        mapper=[
            ("base","BNF"),
            ("soft","S-Unit"),
            ("usm","USM"),
            ("_star","*")
        ],
    )
    
    exper_html += generate_exper4(
        folder_dir="samples/lm",
        experiment_name ="LM Model",
        chosen_files = ["200.wav","656.wav","746.wav"],
        mapper=[
            ("base","BNF"),
            ("soft","S-Unit"),
            ("usm","USM"),
            ("_star","*")
        ],
    )
        
    exper_html += generate_exper4(
        folder_dir="samples/diffusion",
        experiment_name ="Diffusion Model",
        chosen_files=["F2F-225.wav","F2M-96.wav","M2F-30.wav"],
        mapper=[
            ("base","BNF"),
            ("soft","S-Unit"),
            ("usm","USM"),
            ("_star","*")
        ],
    )
    
    put_into_page(
        exper_html,
        title="VC Demo Page",
        big_header="VC Demo",
        sub_header="Mitigating Timbre Leakage with Universal Semantic Mapping Residual Block for Voice Conversion",
        abstract=abstract,
        html_path="index.html"
    )