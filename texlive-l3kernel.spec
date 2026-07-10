%global tl_name l3kernel
%global tl_revision 79405

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX3 programming conventions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/required/l3kernel
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/l3kernel.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/l3kernel.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/l3kernel.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(l3backend)
Requires:	texlive(lua-uni-algos)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The l3kernel bundle provides an implementation of the LaTeX3
programmers' interface, as a set of packages that run under LaTeX2e. The
interface provides the foundation on which the LaTeX3 kernel and other
future code are built: it is an API for TeX programmers. The packages
are set up so that the LaTeX3 conventions can be used with regular
LaTeX2e packages.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/l3kernel
%dir %{_datadir}/texmf-dist/source/latex/l3kernel
%dir %{_datadir}/texmf-dist/tex/latex/l3kernel
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/CHANGELOG.md
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/README.md
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/expl3.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/interface3.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/interface3.tex
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3doc.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3docstrip.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news.tex
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news01.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news01.tex
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news02.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news02.tex
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news03.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news03.tex
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news04.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news04.tex
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news05.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news05.tex
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news06.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news06.tex
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news07.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news07.tex
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news08.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news08.tex
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news09.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news09.tex
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news10.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news10.tex
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news11.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news11.tex
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news12.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3news12.tex
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3obsolete.txt
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3prefixes.csv
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3prefixes.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3prefixes.tex
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3styleguide.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3styleguide.tex
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3syntax-changes.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3syntax-changes.tex
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3term-glossary.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/l3term-glossary.tex
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/source3.pdf
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/source3.tex
%doc %{_datadir}/texmf-dist/doc/latex/l3kernel/source3body.tex
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/expl3.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3.ins
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3basics.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3benchmark.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3bitset.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3bootstrap.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3box.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3cctab.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3clist.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3coffins.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3color.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3debug.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3deprecation.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3doc.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3docstrip.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3expan.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3file.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3flag.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3fp-assign.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3fp-aux.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3fp-basics.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3fp-convert.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3fp-expo.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3fp-extended.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3fp-functions.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3fp-logic.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3fp-parse.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3fp-random.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3fp-round.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3fp-symbolic.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3fp-traps.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3fp-trig.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3fp-types.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3fp.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3fparray.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3graphics.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3int.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3intarray.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3kernel-functions.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3keys.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3legacy.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3luatex.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3msg.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3names.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3opacity.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3pdf.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3prg.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3prop.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3quark.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3regex.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3seq.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3skip.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3sort.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3str-convert.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3str-format.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3str.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3sys.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3text-case.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3text-map.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3text-purify.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3text-utils.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3text.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3tl-analysis.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3tl-build.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3tl.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3token.dtx
%doc %{_datadir}/texmf-dist/source/latex/l3kernel/l3unicode.dtx
%{_datadir}/texmf-dist/tex/latex/l3kernel/expl3-code.tex
%{_datadir}/texmf-dist/tex/latex/l3kernel/expl3-generic.tex
%{_datadir}/texmf-dist/tex/latex/l3kernel/expl3.ltx
%{_datadir}/texmf-dist/tex/latex/l3kernel/expl3.lua
%{_datadir}/texmf-dist/tex/latex/l3kernel/expl3.sty
%{_datadir}/texmf-dist/tex/latex/l3kernel/l3debug.def
%{_datadir}/texmf-dist/tex/latex/l3kernel/l3doc.cls
%{_datadir}/texmf-dist/tex/latex/l3kernel/l3docstrip.tex
%{_datadir}/texmf-dist/tex/latex/l3kernel/l3str-enc-iso88591.def
%{_datadir}/texmf-dist/tex/latex/l3kernel/l3str-enc-iso885910.def
%{_datadir}/texmf-dist/tex/latex/l3kernel/l3str-enc-iso885911.def
%{_datadir}/texmf-dist/tex/latex/l3kernel/l3str-enc-iso885913.def
%{_datadir}/texmf-dist/tex/latex/l3kernel/l3str-enc-iso885914.def
%{_datadir}/texmf-dist/tex/latex/l3kernel/l3str-enc-iso885915.def
%{_datadir}/texmf-dist/tex/latex/l3kernel/l3str-enc-iso885916.def
%{_datadir}/texmf-dist/tex/latex/l3kernel/l3str-enc-iso88592.def
%{_datadir}/texmf-dist/tex/latex/l3kernel/l3str-enc-iso88593.def
%{_datadir}/texmf-dist/tex/latex/l3kernel/l3str-enc-iso88594.def
%{_datadir}/texmf-dist/tex/latex/l3kernel/l3str-enc-iso88595.def
%{_datadir}/texmf-dist/tex/latex/l3kernel/l3str-enc-iso88596.def
%{_datadir}/texmf-dist/tex/latex/l3kernel/l3str-enc-iso88597.def
%{_datadir}/texmf-dist/tex/latex/l3kernel/l3str-enc-iso88598.def
%{_datadir}/texmf-dist/tex/latex/l3kernel/l3str-enc-iso88599.def
