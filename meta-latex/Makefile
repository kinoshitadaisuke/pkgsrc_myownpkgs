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

# fonts
DEPENDS+=	arphic-ttf>=0:../../fonts/arphic-ttf
DEPENDS+=	ipaexfont>=0:../../fonts/ipaexfont
DEPENDS+=	ipafont>=0:../../fonts/ipafont
DEPENDS+=	tex-arphic>=0:../../fonts/tex-arphic
DEPENDS+=	tex-arphic-ttf>=0:../../fonts/tex-arphic-ttf
DEPENDS+=	tex-ascmac>=0:../../fonts/tex-ascmac
DEPENDS+=	tex-ec>=0:../../fonts/tex-ec
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
DEPENDS+=	tex-beamer>=0:../../print/tex-beamer
DEPENDS+=	tex-beamertheme-metropolis>=0:../../print/tex-beamertheme-metropolis
DEPENDS+=	tex-cjk>=0:../../print/tex-cjk
DEPENDS+=	tex-cjkutils>=0:../../print/tex-cjkutils
DEPENDS+=	tex-fancybox>=0:../../print/tex-fancybox
DEPENDS+=	tex-fancyhdr>=0:../../print/tex-fancyhdr
DEPENDS+=	tex-fancyvrb>=0:../../print/tex-fancyvrb
DEPENDS+=	tex-tcolorbox>=0:../../print/tex-tcolorbox

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
