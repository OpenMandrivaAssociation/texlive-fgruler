%global tl_name fgruler
%global tl_revision 77333

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7
Release:	%{tl_revision}.1
Summary:	Draw rulers on the foreground or in the text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fgruler
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fgruler.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fgruler.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fgruler.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package draws horizontal and vertical rulers on the foreground of
every (or the current) page at absolute positions. In this way, you can
check the page layout dimensions. You can also draw various rulers in
the text. The fgruler package requires the services of the following
packages: kvoptions, etoolbox, xcolor, graphicx, eso-pic.

