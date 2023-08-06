# plastidUtilis

`plastidUtilis` is a collection utilities of module which could be applied in manual annotation of plastid genome.



## How to get it?

```shell
# pip install biopython
pip install plastidUtilis
```



## How to use it?

Note: this toolkit is only compatible with TBtools, so be careful with other format in this version.

```shell
# main utilities
python -m plastidUtilis.Sort -f <Geseq_out_seq> -o <name_of_output> --header <Input_header>
python -m plastidUtilis.AbnormalDetect -a <input_fasta> -o <output_filename>
python -m plastidUtilis.BLAST -d <tRNA_database> -t <sort_tRNA> -o <output.fasta>
python -m plastidUtilis.Table2GBK -t <self-made table file> -o <.gb>
python -m plastidUtilis.Filter -f <input_fasta> -i <minumum_length> -I <maximum_length> -o <output filename>
python -m plastidUtilis.Longest -f <input.fasta> -d <delimiter> -o <output.fasta>

# side utilities
python -m plastidUtilis.Translate -i <sorted_CDS> -o <output_protein_sequence>
python -m plastidUtilis.Stats -i <sorted_CDS>    # further it will be designed as tabular output 
python -m plastidUtilis.SequenceAppend -f <input_assembly> -i <input_abnormal_bed> -n <the_number_of_extending_bp> -o <output>
```



# Pipeline





# License

MIT License
Copyright (c) 2022 Zihao Huang, Youpu-Chen.
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.