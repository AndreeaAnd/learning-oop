import sys
from pathlib import Path


src_path: Path = Path(sys.argv[1])
dest_path = Path(sys.argv[1] + '-out.txt')
print(src_path)

try:
    with src_path.open() as src, dest_path.open(mode='x') as dest:
        for line in src_path:
            output_line = line.replace('a', 'x')
            output_line = output_line.replace('A', 'X')
            dest.write(output_line)
except OSError as error:
    print('A file error was occured', error)
    