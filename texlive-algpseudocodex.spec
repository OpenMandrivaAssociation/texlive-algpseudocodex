Name:		texlive-algpseudocodex
Version:	66924
Release:	1
Summary:	Package for typesetting pseudocode
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/algpseudocodex
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/algpseudocodex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/algpseudocodex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows typesetting pseudocode in LaTeX. It is
based on algpseudocode from the algorithmicx package and uses
the same syntax, but adds several new features and
improvements. Notable features include customizable indent
guide lines and the ability to draw boxes around parts of the
code for highlighting differences. This package also has better
support for long code lines spanning several lines and improved
comments.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/algpseudocodex
%doc %{_texmfdistdir}/doc/latex/algpseudocodex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
