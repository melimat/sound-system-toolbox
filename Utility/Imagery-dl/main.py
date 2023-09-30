from downloader import downloadImagery

import argparse
import json



def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--def_file", type=str)

    args = parser.parse_args()
    print(args)

    with open(args.def_file, "r") as config_file:
        json_conf_obj = json.load(config_file)

        width_min = float(json_conf_obj["left_bottom_corner"]["width"])
        length_min = float(json_conf_obj["left_bottom_corner"]["length"])
        width_max = float(json_conf_obj["right_top_corner"]["width"])
        length_max = float(json_conf_obj["right_top_corner"]["length"])
        resolution = float(json_conf_obj["resolution"])
        product_name = str(json_conf_obj["out_name"])
        folder_path = str(json_conf_obj["out_dir"])

        downloadImagery(width_min, length_min, width_max, length_max, resolution, folder_path, product_name)

if __name__ == "__main__":
    run()