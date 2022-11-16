Name:		texlive-fgruler
Version:	63721
Release:	1
Summary:	Draw rulers on the foreground or in the text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fgruler
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fgruler.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fgruler.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fgruler.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package draws horizontal and vertical rulers on the
foreground of every (or the current) page at absolute
positions. In this way, you can check the page layout
dimensions. You can also draw various rulers in the text. The
fgruler package requires the services of the following
packages: kvoptions, etoolbox, xcolor, graphicx, eso-pic.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/fgruler
%{_texmfdistdir}/tex/latex/fgruler
%doc %{_texmfdistdir}/doc/latex/fgruler

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
