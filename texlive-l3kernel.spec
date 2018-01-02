Name:		texlive-l3kernel
Epoch:		1
Version:	20171216
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
%{_texmfdistdir}/tex/latex/l3kernel
%doc %{_texmfdistdir}/doc/latex/l3kernel
#- source
%doc %{_texmfdistdir}/source/latex/l3kernel

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
