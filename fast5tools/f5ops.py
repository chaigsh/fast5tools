## JOHN URBAN (2015, 2016)

import os
######################### processing functions ######
#### e.g. used in:
#### fast5tofastx.py, 
#################################################
def get_comments(request, f5, readtype, samflag=''):
    if not request:
        return False
    elif request in ('base_info', 'pore_info', 'read_stats', 'event_stats', 'read_event_stats', 'abspath', 'filename'):
        if request == 'base_info':
            return samflag + f5.get_base_info_name()
        elif request == 'pore_info':
            return samflag + f5.get_pore_info_name(readtype)
        elif request == 'read_stats':
            return samflag + f5.get_read_stats_name(readtype)
        elif request == 'event_stats':
            return samflag + f5.get_event_stats_name(readtype)
        elif request == 'read_event_stats':
            return samflag + f5.get_read_and_event_stats_name(readtype)
        elif request == 'abspath':
            return samflag + f5.abspath
        elif request == 'filename':
            return samflag + f5.filebasename
    else:
        return samflag + request
    
def get_single_read(f5, readtype, minlen, maxlen, minq, maxq, output, *args, **kwargs):
    ''' f5 is Fast5 object.
        readtype in template, complement, 2d, molecule, all.
        minlen/maxlen - integers.
        minq/maxq - floats
        output is a function'''
    if f5.has_read(readtype):
        if f5.get_seq_len(readtype) >= minlen and f5.get_seq_len(readtype) <= maxlen:
            if f5.get_mean_qscore(readtype) >= minq and f5.get_mean_qscore(readtype) <= maxq:
                if kwargs['comments']:
                    kwargs['comments'] = get_comments(kwargs['comments'], f5, readtype, kwargs['samflag'])
                return output(f5, readtype, *args, **kwargs)

def get_template_read(f5, minlen, maxlen, minq, maxq, output, *args, **kwargs):
    return get_single_read(f5, "template", minlen, maxlen, minq, maxq, output, *args, **kwargs)

def get_complement_read(f5, minlen, maxlen, minq, maxq, output, *args, **kwargs):
    return get_single_read(f5, "complement", minlen, maxlen, minq, maxq, output, *args, **kwargs)

def get_2d_read(f5, minlen, maxlen, minq, maxq, output, *args, **kwargs):
    return get_single_read(f5, "2d", minlen, maxlen, minq, maxq, output, *args, **kwargs)

def get_molecule_read(f5, minlen, maxlen, minq, maxq, output, *args, **kwargs):
    return get_single_read(f5, f5.use_molecule(), minlen, maxlen, minq, maxq, output, *args, **kwargs)

def get_molequal_read(f5, minlen, maxlen, minq, maxq, output, *args, **kwargs):
    return get_single_read(f5, f5.use_molequal(), minlen, maxlen, minq, maxq, output, *args, **kwargs)


def get_all_reads(f5, minlen, maxlen, minq, maxq, output, *args, **kwargs):
    allreads = ""
    for readtype in ["template", "complement", "2d"]:
        try:
            allreads += get_single_read(f5, readtype, minlen, maxlen, minq, maxq, output, *args, **kwargs) + '\n'
        except:
            pass
    return allreads.rstrip()



######################### output functions ######
#### e.g. used in get_single_read()
#################################################


def fastq(f5, readtype, *args, **kwargs):
    return f5.get_fastq(readtype, comments=kwargs['comments'])

def fastq_with_abspath(f5, readtype, *args, **kwargs):
    return f5.get_fastq_with_abspath(readtype, comments=kwargs['comments'])

def fastq_only_abspath(f5, readtype, *args, **kwargs):
    return f5.get_fastq_only_abspath(readtype, comments=kwargs['comments'])

def fastq_with_filename(f5, readtype, *args, **kwargs):
    return f5.get_fastq_with_filename(readtype, comments=kwargs['comments'])

def fastq_only_filename(f5, readtype, *args, **kwargs):
    return f5.get_fastq_only_filename(readtype, comments=kwargs['comments'])

def fastq_readstatsname(f5, readtype, *args, **kwargs):
    name = f5.get_read_stats_name(readtype)
    return f5.get_fastq(readtype, name = name, comments=kwargs['comments'])

def fastq_readstatsname_with_filename(f5, readtype, *args, **kwargs):
    name = f5.get_read_stats_name_with_filebasename(readtype)
    return f5.get_fastq(readtype, name = name, comments=kwargs['comments'])

def fastq_readstatsname_with_abspath(f5, readtype, *args, **kwargs):
    name = f5.get_read_stats_name_with_abspath(readtype)
    return f5.get_fastq(readtype, name = name, comments=kwargs['comments'])




def fasta(f5, readtype, *args, **kwargs):
    return f5.get_fasta(readtype, comments=kwargs['comments'])

def fasta_with_abspath(f5, readtype, *args, **kwargs):
    return f5.get_fasta_with_abspath(readtype, comments=kwargs['comments'])

def fasta_only_abspath(f5, readtype, *args, **kwargs):
    return f5.get_fasta_only_abspath(readtype, comments=kwargs['comments'])

def fasta_with_filename(f5, readtype, *args, **kwargs):
    return f5.get_fasta_with_filename(readtype, comments=kwargs['comments'])

def fasta_only_filename(f5, readtype, *args, **kwargs):
    return f5.get_fasta_only_filename(readtype, comments=kwargs['comments'])

def fasta_readstatsname(f5, readtype, *args, **kwargs):
    name = f5.get_read_stats_name(readtype)
    return f5.get_fasta(readtype, name = name, comments=kwargs['comments'])

def fasta_readstatsname_with_filename(f5, readtype, *args, **kwargs):
    name = f5.get_read_stats_name_with_filebasename(readtype)
    return f5.get_fasta(readtype, name = name, comments=kwargs['comments'])

def fasta_readstatsname_with_abspath(f5, readtype, *args, **kwargs):
    name = f5.get_read_stats_name_with_abspath(readtype)
    return f5.get_fasta(readtype, name = name, comments=kwargs['comments'])



def qual(f5, readtype, *args, **kwargs):
    return f5.get_quals(readtype, comments=kwargs['comments'])

def qual_with_abspath(f5, readtype, *args, **kwargs):
    return f5.get_quals_with_abspath(readtype, comments=kwargs['comments'])

def qual_only_abspath(f5, readtype, *args, **kwargs):
    return f5.get_quals_only_abspath(readtype, comments=kwargs['comments'])

def qual_with_filename(f5, readtype, *args, **kwargs):
    return f5.get_quals_with_filename(readtype, comments=kwargs['comments'])

def qual_only_filename(f5, readtype, *args, **kwargs):
    return f5.get_quals_only_filename(readtype, comments=kwargs['comments'])


def qual_readstatsname(f5, readtype, *args, **kwargs):
    name = f5.get_read_stats_name(readtype)
    return f5.get_quals(readtype, name = name, comments=kwargs['comments'])

def qual_readstatsname_with_filename(f5, readtype, *args, **kwargs):
    name = f5.get_read_stats_name_with_filebasename(readtype)
    return f5.get_quals(readtype, name = name, comments=kwargs['comments'])

def qual_readstatsname_with_abspath(f5, readtype, *args, **kwargs):
    name = f5.get_read_stats_name_with_abspath(readtype)
    return f5.get_quals(readtype, name = name, comments=kwargs['comments'])


def intqual(f5, readtype, *args, **kwargs):
    return f5.get_quals_as_int(readtype)

def oldfalcon(f5, readtype, *args, **kwargs):
    return f5.get_falcon_fasta(readtype, zmw_num=kwargs['falcon_i'], style="old")

def newfalcon(f5, readtype, *args, **kwargs):
    return f5.get_falcon_fasta(readtype, zmw_num=kwargs['falcon_i'], style="new")

#######
f5fxn = {}
f5fxn[1] = lambda f5: f5.get_base_info_name()
f5fxn[2] = lambda f5: f5.get_seq_len(f5.use_molecule()) if f5.has_reads() else "-"
f5fxn[3] = lambda f5: f5.get_mean_qscore(f5.use_molecule()) if f5.has_reads() else "-"
f5fxn[4] = lambda f5: 1 if f5.has_read("complement") else 0
f5fxn[5] = lambda f5: 1 if f5.has_read("2d") else 0
f5fxn[6] = lambda f5: f5.get_seq_len("2d") if f5.has_read("2d") else "-"
f5fxn[7] = lambda f5: f5.get_seq_len("template") if f5.has_read("template") else "-"
f5fxn[8] = lambda f5: f5.get_seq_len("complement") if f5.has_read("complement") else "-"
f5fxn[9] = lambda f5: f5.get_mean_qscore("2d") if f5.has_read("2d") else "-"
f5fxn[10] = lambda f5: f5.get_mean_qscore("template") if f5.has_read("template") else "-"
f5fxn[11] = lambda f5: f5.get_mean_qscore("complement") if f5.has_read("complement") else "-"
f5fxn[12] = lambda f5: f5.get_num_events("input")
f5fxn[13] = lambda f5: f5.get_num_events("template") if f5.has_read("template") else "-"
f5fxn[14] = lambda f5: f5.get_num_events("complement") if f5.has_read("complement") else "-"
f5fxn[15] = lambda f5: f5.get_num_called_events("template") if f5.has_read("template") else "-"
f5fxn[16] = lambda f5: f5.get_num_called_events("complement") if f5.has_read("complement") else "-"
f5fxn[17] = lambda f5: f5.get_num_skips("template") if f5.has_read("template") else "-"
f5fxn[18] = lambda f5: f5.get_num_skips("complement") if f5.has_read("complement") else "-"
f5fxn[19] = lambda f5: f5.filename
f5fxn[20] = lambda f5: f5.abspath
f5fxn[21] = lambda f5: f5.get_log()
f5fxn[22] = lambda f5: f5.get_log_string()
##f5fxn[19] = lambda f5
##f5fxn[20] = lambda f5
##f5fxn[21] = lambda f5
##f5fxn[22] = lambda f5
##f5fxn[23] = lambda f5
##f5fxn[24] = lambda f5













