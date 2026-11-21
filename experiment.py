import numpy as np
from common import *

def run():
    r=rng(52);x=normalize(r.normal(size=(500,128))).astype('float32');q=normalize(r.normal(size=(50,128))).astype('float32')
    exact=np.argsort(-(q@x.T),axis=1)[:,:10];binary=np.packbits(x>=0,axis=1);qb=np.packbits(q>=0,axis=1)
    distances=np.unpackbits(np.bitwise_xor(qb[:,None,:],binary[None,:,:]),axis=-1).sum(-1)
    approx=np.argsort(distances,axis=1,kind='stable')[:,:10]
    recall=float(np.mean([len(set(a)&set(b))/10 for a,b in zip(exact,approx)]))
    return {'recall_at_10':recall,'float_storage_bytes':x.nbytes,'packed_storage_bytes':binary.nbytes,
            'storage_ratio':x.nbytes/binary.nbytes,'checks':[check(binary.nbytes*32==x.nbytes,'Actual bit packing reduces raw vector storage 32x'),check(distances.shape==(50,500),'Real Hamming distances computed')],
            'scope':'Sign quantization of synthetic vectors. Raw storage excludes index and metadata; no semantic-quality claim.'}
