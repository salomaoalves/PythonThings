from Bio.Seq import Seq
from Bio import SeqIO
from Bio.PDB import *

#SEQUENCIA
seq1 = Seq("ATG") #declara uma sequencia
seqComplementar = seq1.complement() #gera a seq complementar de 'seq1'
seqComplRev = seq1.reverse_complement() #gera a seq reversa complementar de 'seq1'

#TRANSCRIÇÃO
seqRna = seq1.transcribe() #realiza a transcrição
seqDna = seqRna.back_transcribe() #volta para o dna

#TRADUÇÃO
seqProt = seqRna.translate() #realiza a tradução apartir do rna
seqProt2 = seqDna.translate() #realiza a tradução apartir do dna

#SEQUENCIA EM .FASTA
for fasta in SeqIO.parse('seq.fasta','fasta'):
    id = fasta.id #printa o id (cabecalho)
    sequencia = fasta.seq #printa a sequencia

#SMCRA
parser = PDBParser()
estrutura = parser.get_structure("1BGA","1bga.pdb")
atoma100 = estrutura[0]['A'][100]['CA']
atoma101 = estrutura[0]['A'][101]['CA']
difer = atoma100-atoma101