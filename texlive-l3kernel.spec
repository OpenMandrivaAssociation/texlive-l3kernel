Name:		texlive-l3kernel
Epoch:		1
Version:	72755
Release:	1
Summary:	LaTeX3 programming conventions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/l3kernel
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3kernel.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3kernel.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3kernel.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
