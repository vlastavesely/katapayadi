prefix = /usr

bindir = $(prefix)/bin
mandir = $(prefix)/share/man/man1

all: katapayadi.1.gz

katapayadi.1.gz: katapayadi.1
	cat $< | gzip >$@

install:
	install -m 0755 katapayadi.py -T $(bindir)/katapayadi
	install -m 0644 katapayadi.1.gz $(mandir)

uninstall:
	rm -f $(bindir)/katapayadi
	rm -f $(mandir)/katapayadi.1.gz

clean:
	rm -f katapayadi.1.gz
