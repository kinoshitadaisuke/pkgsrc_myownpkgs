# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-latex-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs graphics print
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for basic tools
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# devel
DEPENDS+=	tex-pgfopts>=0:../../devel/tex-pgfopts

# fonts
DEPENDS+=	arphic-ttf>=0:../../fonts/arphic-ttf
DEPENDS+=	gsftopkk>=0:../../fonts/gsftopkk
DEPENDS+=	ipaexfont>=0:../../fonts/ipaexfont
DEPENDS+=	ipafont>=0:../../fonts/ipafont
DEPENDS+=	tex-arphic>=0:../../fonts/tex-arphic
DEPENDS+=	tex-arphic-ttf>=0:../../fonts/tex-arphic-ttf
DEPENDS+=	tex-ascmac>=0:../../fonts/tex-ascmac
DEPENDS+=	tex-ec>=0:../../fonts/tex-ec
DEPENDS+=	tex-haranoaji>=0:../../fonts/tex-haranoaji
DEPENDS+=	tex-haranoaji-extra>=0:../../fonts/tex-haranoaji-extra
DEPENDS+=	tex-ipaex>=0:../../fonts/tex-ipaex
DEPENDS+=	tex-ipaex-type1>=0:../../fonts/tex-ipaex-type1
DEPENDS+=	tex-metafont>=0:../../fonts/tex-metafont
DEPENDS+=	tex-noto>=0:../../fonts/tex-noto
DEPENDS+=	tex-ttfutils>=0:../../fonts/tex-ttfutils
DEPENDS+=	ttf2pk>=0:../../fonts/ttf2pk

# graphics
DEPENDS+=	tex-pst-node>=0:../../graphics/tex-pst-node
DEPENDS+=	tex-pst-text>=0:../../graphics/tex-pst-text
DEPENDS+=	tex-pst-tools>=0:../../graphics/tex-pst-tools
DEPENDS+=	tex-pstricks>=0:../../graphics/tex-pstricks

# print
DEPENDS+=	cjkutils>=0:../../print/cjkutils
DEPENDS+=	dvipsk>=0:../../print/dvipsk
DEPENDS+=	dvipdfmx>=0:../../print/dvipdfmx
DEPENDS+=	tex-a0poster>=0:../../print/tex-a0poster
DEPENDS+=	tex-beamer>=0:../../print/tex-beamer
DEPENDS+=	tex-beamertheme-focus>=0:../../print/tex-beamertheme-focus
DEPENDS+=	tex-beamertheme-metropolis>=0:../../print/tex-beamertheme-metropolis
DEPENDS+=	tex-cjk>=0:../../print/tex-cjk
DEPENDS+=	tex-cjkutils>=0:../../print/tex-cjkutils
DEPENDS+=	tex-ctable>=0:../../print/tex-ctable
DEPENDS+=	tex-fancybox>=0:../../print/tex-fancybox
DEPENDS+=	tex-fancyhdr>=0:../../print/tex-fancyhdr
DEPENDS+=	tex-fancyvrb>=0:../../print/tex-fancyvrb
DEPENDS+=	tex-listings>=0:../../print/tex-listings
DEPENDS+=	tex-luatexja>=0:../../print/tex-luatexja
DEPENDS+=	tex-prosper>=0:../../print/tex-prosper
DEPENDS+=	tex-tcolorbox>=0:../../print/tex-tcolorbox
DEPENDS+=	tex-titlesec>=0:../../print/tex-titlesec
DEPENDS+=	tex-trimspaces>=0:../../print/tex-trimspaces

# textproc
DEPENDS+=	${PYPKGPREFIX}-pygments>=0:../../textproc/py-pygments

# pkgsrc_myownpkgs
DEPENDS+=	tex-beamertheme-amurmaple>=0:../../pkgsrc_myownpkgs/tex-beamertheme-amurmaple
DEPENDS+=	tex-beamertheme-arguelles>=0:../../pkgsrc_myownpkgs/tex-beamertheme-arguelles
DEPENDS+=	tex-beamertheme-simpledarkblue>=0:../../pkgsrc_myownpkgs/tex-beamertheme-simpledarkblue
DEPENDS+=	tex-beamertheme-simpleplus>=0:../../pkgsrc_myownpkgs/tex-beamertheme-simpleplus
DEPENDS+=	tex-beamertheme-tcolorbox>=0:../../pkgsrc_myownpkgs/tex-beamertheme-tcolorbox
DEPENDS+=	tex-beamertheme-trigon>=0:../../pkgsrc_myownpkgs/tex-beamertheme-trigon
DEPENDS+=	tex-pdfcol>=0:../../pkgsrc_myownpkgs/tex-pdfcol
DEPENDS+=	tex-tikzfill>=0:../../pkgsrc_myownpkgs/tex-tikzfill

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
