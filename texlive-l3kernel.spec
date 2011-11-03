# revision 24256
# category Package
# catalog-ctan /macros/latex/contrib/l3kernel
# catalog-date 2011-10-10 01:01:54 +0200
# catalog-license lppl1.3
# catalog-version SVN 2900
Name:		texlive-l3kernel
Version:	0.2900
Release:	1
Summary:	LaTeX3 programming conventions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/l3kernel
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3kernel.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3kernel.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3kernel.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The l3kernel bundle provides an implementation of the LaTeX3
programmers' interface, as a set of packages that run under
LaTeX 2e. The interface provides the foundation on which the
LaTeX3 kernel and other future code are built: it is an API for
TeX programmers. The packages are set up so that the LaTeX3
conventions can be used with regular LaTeX 2e packages. All the
files of the bundle are also available in the Subversion (SVN)
repository of the LaTeX3 Project. The bundle on CTAN is based
on a snapshot of the SVN repository on 2011-10-09.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/l3kernel/l3doc.ist
%{_texmfdistdir}/tex/latex/l3kernel/expl3.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3basics.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3bootstrap.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3box.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3clist.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3coffins.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3color.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3doc.cls
%{_texmfdistdir}/tex/latex/l3kernel/l3expan.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3file.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3fp.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3int.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3io.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3keys.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3luatex.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3msg.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3names.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3prg.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3prop.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3quark.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3seq.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3skip.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3tl.sty
%{_texmfdistdir}/tex/latex/l3kernel/l3token.sty
%doc %{_texmfdistdir}/doc/latex/l3kernel/README
%doc %{_texmfdistdir}/doc/latex/l3kernel/expl3.pdf
%doc %{_texmfdistdir}/doc/latex/l3kernel/interface3.pdf
%doc %{_texmfdistdir}/doc/latex/l3kernel/interface3.tex
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
%doc %{_texmfdistdir}/source/latex/l3kernel/l3clist.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3coffins.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3color.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3doc.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3drivers.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3expan.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3file.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3final.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3fp.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3int.dtx
%doc %{_texmfdistdir}/source/latex/l3kernel/l3io.dtx
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
%doc %{_texmfdistdir}/source/latex/l3kernel/l3toks.dtx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
