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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
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

