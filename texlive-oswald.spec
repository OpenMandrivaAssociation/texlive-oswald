Name:		texlive-oswald
Version:	60784
Release:	2
Summary:	The Oswald family of fonts with support for LaTeX and pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/oswald
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oswald.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oswald.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the Oswald family of fonts, designed by
Vernon Adams, Kalapi Gajjar, Cyreal, with support for LaTeX and
pdfLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/oswald
%{_texmfdistdir}/fonts/vf/public/oswald
%{_texmfdistdir}/fonts/type1/public/oswald
%{_texmfdistdir}/fonts/tfm/public/oswald
%{_texmfdistdir}/fonts/map/dvips/oswald
%{_texmfdistdir}/fonts/enc/dvips/oswald
%doc %{_texmfdistdir}/doc/fonts/oswald

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
