# revision 32204
# category Package
# catalog-ctan /macros/latex/contrib/l3kernel
# catalog-date 2013-11-19 19:33:53 +0100
# catalog-license lppl1.3
# catalog-version SVN 4610
Name:		texlive-l3kernel
Epoch:		1
Version:	SVN4610
Release:	2
Summary:	LaTeX3 programming conventions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/l3kernel
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3kernel.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3kernel.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3kernel.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The l3kernel bundle provides an implementation of the LaTeX3
programmers' interface, as a set of packages that run under
LaTeX 2e. The interface provides the foundation on which the
LaTeX3 kernel and other future code are built: it is an API for
TeX programmers. The packages are set up so that the LaTeX3
conventions can be used with regular LaTeX 2e packages. All the
files of the bundle are also available in the project's
Subversion (SVN) repository.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/l3kernel/l3doc.ist
%{_texmfdistdir}/tex/latex/l3kernel/expl3.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3basics.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3bootstrap.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3box.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3candidates.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3clist.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3coffins.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3color.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3doc.cls
%{_texmfdistdir}/tex/latex/l3kernel/l3docstrip.tex
%{_texmfdistdir}/tex/latex/l3kernel/l3dvipdfmx.def
%{_texmfdistdir}/tex/latex/l3kernel/l3dvips.def
%{_texmfdistdir}/tex/latex/l3kernel/l3expan.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3file.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3fp.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3int.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3keys.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3luatex.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3msg.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3names.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3pdfmode.def
%{_texmfdistdir}/tex/latex/l3kernel/l3prg.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3prop.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3quark.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3seq.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3skip.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3tl.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3token.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3xdvipdfmx.def
%doc %{_texmfdistdir}/doc/latex/l3kernel/README
%doc %{_texmfdistdir}/doc/latex/l3kernel/expl3.pdf
%doc %{_texmfdistdir}/doc/latex/l3kernel/interface3.pdf
%doc %{_texmfdistdir}/doc/latex/l3kernel/interface3.tex
%doc %{_texmfdistdir}/doc/latex/l3kernel/l3docstrip.pdf
%doc %{_texmfdistdir}/doc/latex/l3kernel/l3styleguide.pdf
%doc %{_texmfdistdir}/doc/latex/l3kernel/l3styleguide.tex
%doc %{_texmfdistdir}/doc/latex/l3kernel/l3syntax-changes.pdf
%doc %{_texmfdistdir}/doc/latex/l3kernel/l3syntax-changes.tex
%doc %{_texmfdistdir}/doc/latex/l3kernel/source3.pdf
%doc %{_texmfdistdir}/doc/latex/l3kernel/source3.tex
%doc %{_texmfdistdir}/doc/latex/l3kernel/source3body.tex
#- source
%doc %{_texmfdistdir}/source/latex/l3kernel/expl3.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3alloc.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3basics.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3bootstrap.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3box.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3candidates.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3clist.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3coffins.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3color.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3doc.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3docstrip.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3drivers.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3expan.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3file.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3final.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3fp-assign.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3fp-aux.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3fp-basics.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3fp-convert.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3fp-expo.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3fp-extended.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3fp-logic.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3fp-old.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3fp-parse.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3fp-round.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3fp-traps.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3fp-trig.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3fp.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3int.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3keys.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3luatex.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3msg.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3names.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3prg.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3prop.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3quark.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3seq.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3skip.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3tl.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3token.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}
