# -*- coding: utf-8 -*-
# author = "Louis"

import numpy
from jina import Document

doc1 = Document(content=text_from_file, mime_type='text/x-python')  # a text document contains python code
doc2 = Document(embedding=numpy.random.random([10, 10]))



if __name__ == '__main__':
    pass
