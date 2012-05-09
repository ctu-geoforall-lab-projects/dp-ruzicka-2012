FILE=thesis

all: $(FILE).pdf

$(FILE).pdf: *.tex Makefile
	make pdf
	@while grep Rerun $(FILE).log >/dev/null 2>&1 ; do \
		make pdf; \
	done

pdf:
	pdflatex $(FILE).tex

clean:
	rm -f *~ *.aux *.log *.out *.toc *.idx *.lol \
	*.bbl *.blg *.ilg *.ind

distclean:
	make clean
	rm -f $(FILE).pdf
