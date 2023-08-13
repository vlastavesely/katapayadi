prefix = /usr

bindir = $(prefix)/bin

all:

install:
	install -m 0755 katapayadi.py -T $(bindir)/katapayadi

uninstall:
	rm -f $(bindir)/katapayadi
