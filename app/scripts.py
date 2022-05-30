import argparse

from scripts.import_autores_dataset.import_autores_dataset import ImportAutoresDataSet

parser = argparse.ArgumentParser(
    description="Rotinas automizadas",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument("script-name", help="nome do script")
parser.add_argument("-f", "--file", help="carregar arquivo")

args = vars(parser.parse_args())
script_name = args.get("script-name")

scripts = {
    "import_autores_dataset": ImportAutoresDataSet
}


def handler_script(script_name):
    script = scripts[script_name]
    args.pop("script-name")
    return script


handler_script(script_name)(**args).action()