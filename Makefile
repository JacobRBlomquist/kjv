PREFIX = /usr/local

wog: wog.sh wog.awk wog.tsv
	cat wog.sh > $@
	echo 'exit 0' >> $@
	echo '#EOF' >> $@
	tar cz wog.awk wog.tsv >> $@
	chmod +x $@

test: wog.sh
	shellcheck -s sh wog.sh

clean:
	rm -f wog 

install: wog 
	mkdir -p $(DESTDIR)$(PREFIX)/bin
	cp -f wog $(DESTDIR)$(PREFIX)/bin
	chmod 755 $(DESTDIR)$(PREFIX)/bin/wog

uninstall:
	rm -f $(DESTDIR)$(PREFIX)/bin/wog

.PHONY: test clean install uninstall
