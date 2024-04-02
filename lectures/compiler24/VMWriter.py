CONSTANT, ARGUMENT, LOCAL, THIS, THAT, POINTER, STATIC, TEMP = range(8)

seg_names = {
    CONSTANT: 'constant',
    ARGUMENT: 'argument'
    # etc.
}

class VMWriter:
    def __init__(self, output_file_name):
        self.f = open(output_file_name, 'w')

    def write_push(self, seg, idx):
        self.f.write(f'push {seg_names[seg]} {idx}\n')

    def write_raw(self, txt):
        self.f.write(txt + '\n')

    def write_call(self, function_name, num_args):
        self.f.write(f'call {function_name} {num_args}\n')
