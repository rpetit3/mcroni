import pytest
import subprocess
import os

import mcroni.seqFunctions as sf
import mcroni.mcroni as mcroni

# Data directory
#data_dir = dir+'/../data'

# Generating fake test data

# 1. Fake variant file for classify_variant()
fake_variant_file = 'fake_variant.fa'
with open(fake_variant_file, 'w') as f: # make a fake fasta file
    f.write('>FAKE_1\nAAA\n>FAKE_2\nTTT')

# 2. Fake mcr-1 + flanking file for cut_region()
fake_mcr_file = 'fake_mcr.fa'
with open(fake_mcr_file, 'w') as f: # make another fake fasta file
    f.write('>FAKE_3\nTTTTTATGATGCAGCATACTTCTGTGTGGTACCGACGCTCGGTCAGTCCGTTTGTTCTTGTGGCGAGTGTTGCCGTTTTCTTGACCGCGACCGCCAATCTTACCTTTTTTGATAAAATCAGCCAAACCTATCCCATCGCGGACAATCTCGGCTTTGTGCTGACGATCGCTGTCGTGCTCTTTGGCGCGATGCTACTGATCACCACGCTGTTATCATCGTATCGCTATGTGCTAAAGCCTGTGTTGATTTTGCTATTAATCATGGGCGCGGTGACCAGTTATTTTACTGACACTTATGGCACGGTCTATGATACGACCATGCTCCAAAATGCCCTACAGACCGACCAAGCCGAGACCAAGGATCTATTAAACGCAGCGTTTATCATGCGTATCATTGGTTTGGGTGTGCTACCAAGTTTGCTTGTGGCTTTTGTTAAGGTGGATTATCCGACTTGGGGCAAGGGTTTGATGCGCCGATTGGGCTTGATCGTGGCAAGTCTTGCGCTGATTTTACTGCCTGTGGTGGCGTTCAGCAGTCATTATGCCAGTTTCTTTCGCGTGCATAAGCCGCTGCGTAGCTATGTCAATCCGATCATGCCAATCTACTCGGTGGGTAAGCTTGCCAGTATTGAGTATAAAAAAGCCAGTGCGCCAAAAGATACCATTTATCACGCCAAAGACGCGGTACAAGCAACCAAGCCTGATATGCGTAAGCCACGCCTAGTGGTGTTCGTCGTCGGTGAGACGGCACGCGCCGATCATGTCAGCTTCAATGGCTATGAGCGCGATACTTTCCCACAGCTTGCCAAGATCGATGGCGTGACCAATTTTAGCAATGTCACATCGTGCGGCACATCGACGGCGTATTCTGTGCCGTGTATGTTCAGCTATCTGGGCGCGGATGAGTATGATGTCGATACCGCCAAATACCAAGAAAATGTGCTGGATACGCTGGATCGCTTGGGCGTAAGTATCTTGTGGCGTGATAATAATTCGGACTCAAAAGGCGTGATGGATAAGCTGCCAAAAGCGCAATTTGCCGATTATAAATCCGCGACCAACAACGCCATCTGCAACACCAATCCTTATAACGAATGCCGCGATGTCGGTATGCTCGTTGGCTTAGATGACTTTGTCGCTGCCAATAACGGCAAAGATATGCTGATCATGCTGCACCAAATGGGCAATCACGGGCCTGCGTATTTTAAGCGATATGATGAAAAGTTTGCCAAATTCACGCCAGTGTGTGAAGGTAATGAGCTTGCCAAGTGCGAACATCAGTCCTTGATCAATGCTTATGACAATGCCTTGCTTGCCACCGATGATTTCATCGCTCAAAGTATCCAGTGGCTGCAGACGCACAGCAATGCCTATGATGTCTCAATGCTGTATGTCAGCGATCATGGCGAAAGTCTGGGTGAGAACGGTGTCTATCTACATGGTATGCCAAATGCCTTTGCACCAAAAGAACAGCGCAGTGTGCCTGCATTTTTCTGGACGGATAAGCAAACTGGCATCACGCCAATGGCAACCGATACCGTCCTGACCCATGACGCGATCACGCCGACATTATTAAAGCTGTTTGATGTCACCGCGGACAAAGTCAAAGACCGCACCGCATTCATCCGCTGATTTTT')

#### TESTS ####
def test_trivial_variant_is_classified_correctly_by_classify_variant():
      assert sf.classify_variant('AAA', variants_db=fake_variant_file)=='FAKE_1'

def test_upstream_padding_by_cut_region_works():
    assert mcroni.cut_region(fake_mcr_file, upstream_bases=6, downstream_bases=0)=='-TTTTTATGATGCAGCATACTTCTGTGTGGTACCGACGCTCGGTCAGTCCGTTTGTTCTTGTGGCGAGTGTTGCCGTTTTCTTGACCGCGACCGCCAATCTTACCTTTTTTGATAAAATCAGCCAAACCTATCCCATCGCGGACAATCTCGGCTTTGTGCTGACGATCGCTGTCGTGCTCTTTGGCGCGATGCTACTGATCACCACGCTGTTATCATCGTATCGCTATGTGCTAAAGCCTGTGTTGATTTTGCTATTAATCATGGGCGCGGTGACCAGTTATTTTACTGACACTTATGGCACGGTCTATGATACGACCATGCTCCAAAATGCCCTACAGACCGACCAAGCCGAGACCAAGGATCTATTAAACGCAGCGTTTATCATGCGTATCATTGGTTTGGGTGTGCTACCAAGTTTGCTTGTGGCTTTTGTTAAGGTGGATTATCCGACTTGGGGCAAGGGTTTGATGCGCCGATTGGGCTTGATCGTGGCAAGTCTTGCGCTGATTTTACTGCCTGTGGTGGCGTTCAGCAGTCATTATGCCAGTTTCTTTCGCGTGCATAAGCCGCTGCGTAGCTATGTCAATCCGATCATGCCAATCTACTCGGTGGGTAAGCTTGCCAGTATTGAGTATAAAAAAGCCAGTGCGCCAAAAGATACCATTTATCACGCCAAAGACGCGGTACAAGCAACCAAGCCTGATATGCGTAAGCCACGCCTAGTGGTGTTCGTCGTCGGTGAGACGGCACGCGCCGATCATGTCAGCTTCAATGGCTATGAGCGCGATACTTTCCCACAGCTTGCCAAGATCGATGGCGTGACCAATTTTAGCAATGTCACATCGTGCGGCACATCGACGGCGTATTCTGTGCCGTGTATGTTCAGCTATCTGGGCGCGGATGAGTATGATGTCGATACCGCCAAATACCAAGAAAATGTGCTGGATACGCTGGATCGCTTGGGCGTAAGTATCTTGTGGCGTGATAATAATTCGGACTCAAAAGGCGTGATGGATAAGCTGCCAAAAGCGCAATTTGCCGATTATAAATCCGCGACCAACAACGCCATCTGCAACACCAATCCTTATAACGAATGCCGCGATGTCGGTATGCTCGTTGGCTTAGATGACTTTGTCGCTGCCAATAACGGCAAAGATATGCTGATCATGCTGCACCAAATGGGCAATCACGGGCCTGCGTATTTTAAGCGATATGATGAAAAGTTTGCCAAATTCACGCCAGTGTGTGAAGGTAATGAGCTTGCCAAGTGCGAACATCAGTCCTTGATCAATGCTTATGACAATGCCTTGCTTGCCACCGATGATTTCATCGCTCAAAGTATCCAGTGGCTGCAGACGCACAGCAATGCCTATGATGTCTCAATGCTGTATGTCAGCGATCATGGCGAAAGTCTGGGTGAGAACGGTGTCTATCTACATGGTATGCCAAATGCCTTTGCACCAAAAGAACAGCGCAGTGTGCCTGCATTTTTCTGGACGGATAAGCAAACTGGCATCACGCCAATGGCAACCGATACCGTCCTGACCCATGACGCGATCACGCCGACATTATTAAAGCTGTTTGATGTCACCGCGGACAAAGTCAAAGACCGCACCGCATTCATCCGCTGA'

def test_downstream_padding_by_cut_region_works():
    assert mcroni.cut_region(fake_mcr_file, upstream_bases=0, downstream_bases=6)=='ATGATGCAGCATACTTCTGTGTGGTACCGACGCTCGGTCAGTCCGTTTGTTCTTGTGGCGAGTGTTGCCGTTTTCTTGACCGCGACCGCCAATCTTACCTTTTTTGATAAAATCAGCCAAACCTATCCCATCGCGGACAATCTCGGCTTTGTGCTGACGATCGCTGTCGTGCTCTTTGGCGCGATGCTACTGATCACCACGCTGTTATCATCGTATCGCTATGTGCTAAAGCCTGTGTTGATTTTGCTATTAATCATGGGCGCGGTGACCAGTTATTTTACTGACACTTATGGCACGGTCTATGATACGACCATGCTCCAAAATGCCCTACAGACCGACCAAGCCGAGACCAAGGATCTATTAAACGCAGCGTTTATCATGCGTATCATTGGTTTGGGTGTGCTACCAAGTTTGCTTGTGGCTTTTGTTAAGGTGGATTATCCGACTTGGGGCAAGGGTTTGATGCGCCGATTGGGCTTGATCGTGGCAAGTCTTGCGCTGATTTTACTGCCTGTGGTGGCGTTCAGCAGTCATTATGCCAGTTTCTTTCGCGTGCATAAGCCGCTGCGTAGCTATGTCAATCCGATCATGCCAATCTACTCGGTGGGTAAGCTTGCCAGTATTGAGTATAAAAAAGCCAGTGCGCCAAAAGATACCATTTATCACGCCAAAGACGCGGTACAAGCAACCAAGCCTGATATGCGTAAGCCACGCCTAGTGGTGTTCGTCGTCGGTGAGACGGCACGCGCCGATCATGTCAGCTTCAATGGCTATGAGCGCGATACTTTCCCACAGCTTGCCAAGATCGATGGCGTGACCAATTTTAGCAATGTCACATCGTGCGGCACATCGACGGCGTATTCTGTGCCGTGTATGTTCAGCTATCTGGGCGCGGATGAGTATGATGTCGATACCGCCAAATACCAAGAAAATGTGCTGGATACGCTGGATCGCTTGGGCGTAAGTATCTTGTGGCGTGATAATAATTCGGACTCAAAAGGCGTGATGGATAAGCTGCCAAAAGCGCAATTTGCCGATTATAAATCCGCGACCAACAACGCCATCTGCAACACCAATCCTTATAACGAATGCCGCGATGTCGGTATGCTCGTTGGCTTAGATGACTTTGTCGCTGCCAATAACGGCAAAGATATGCTGATCATGCTGCACCAAATGGGCAATCACGGGCCTGCGTATTTTAAGCGATATGATGAAAAGTTTGCCAAATTCACGCCAGTGTGTGAAGGTAATGAGCTTGCCAAGTGCGAACATCAGTCCTTGATCAATGCTTATGACAATGCCTTGCTTGCCACCGATGATTTCATCGCTCAAAGTATCCAGTGGCTGCAGACGCACAGCAATGCCTATGATGTCTCAATGCTGTATGTCAGCGATCATGGCGAAAGTCTGGGTGAGAACGGTGTCTATCTACATGGTATGCCAAATGCCTTTGCACCAAAAGAACAGCGCAGTGTGCCTGCATTTTTCTGGACGGATAAGCAAACTGGCATCACGCCAATGGCAACCGATACCGTCCTGACCCATGACGCGATCACGCCGACATTATTAAAGCTGTTTGATGTCACCGCGGACAAAGTCAAAGACCGCACCGCATTCATCCGCTGATTTTT-'

def test_cut_region_warns_when_given_negative_bases():
    '''cut_region should set negative bases to zero'''
    return

def test_mcroni_complains_when_input_file_does_not_exist():
    '''running with nonexistent input file should be handled gracefully'''
    return

def test_mcroni_complains_when_input_file_is_not_fasta():
    '''running with a file that is not a fasta file is handled gracefully'''
    return

def test_mcroni_complains_when_output_file_exists():
    '''specifying output file which already exists gives refusal to run'''
    return

def test_using_force_flag_overwrites_output_file():
    '''using --force flag overwrites an existing output file()'''
    return
