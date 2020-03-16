FIGSRC = ../figures_src
FIGURES = $(wildcard $(FIGSRC)/*.fodg)
FIGPDF = $(FIGURES:$(FIGSRC)/%.fodg=%.pdf)

.PHONY:
all:	$(FIGPDF)

$(FIGPDF): %.pdf: $(FIGSRC)/%.fodg
	libreoffice --headless --convert-to pdf $<
	
.PHONY:	clean
clean:	
	rm -i $(FIGPDF)
