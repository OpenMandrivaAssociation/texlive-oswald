%global tl_name oswald
%global tl_revision 78931

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	The Oswald family of fonts with support for LaTeX and pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/oswald
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/oswald.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/oswald.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package provides the Oswald family of fonts, designed by Vernon
Adams, Kalapi Gajjar, Cyreal, with support for LaTeX and pdfLaTeX.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from oswald:
Map Zeroswald.map
TL_DROPIN_EOF
