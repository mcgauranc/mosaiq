"""Rules"""


def progress(self):
    """Check if foo can send to corge"""
    return True


def is_conformant(self):
    """Check if foo can send to corge"""
    print("should progress: %s" % self.conformant)
    return self.conformant is 'Y'

def is_non_conformant(self):
    """Check if foo can send to corge"""
    print("should progress: %s" % self.conformant)
    return self.conformant is not 'Y'
