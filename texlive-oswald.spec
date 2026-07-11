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
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the Oswald family of fonts, designed by Vernon
Adams, Kalapi Gajjar, Cyreal, with support for LaTeX and pdfLaTeX.

