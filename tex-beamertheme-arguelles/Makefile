# $NetBSD$

DISTNAME=	beamertheme-arguelles
PKGNAME=	tex-${DISTNAME}-2.2.0
TEXLIVE_REV=	66645
CATEGORIES=	print
#MASTER_SITES=	${MASTER_SITE_TEX_CTAN:=systems/texlive/tlnet/archive/}
#EXTRACT_SUFX=	.tar.xz

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	http://www.dnsbalance.ring.gr.jp/pub/text/CTAN/systems/texlive/tlnet/archive/
COMMENT=	Beamer's theme arguelles
LICENSE=	mit

WRKSRC=		${WRKDIR} # TODO: one of tex tlpkg, or leave it as-is
USE_LANGUAGES=	# none

DEPENDS+=	tex-beamer>=0:../../print/tex-beamer
DEPENDS+=	tex-microtype>=0:../../print/tex-microtype
DEPENDS+=	tex-alegreya>=0:../../fonts/tex-alegreya
DEPENDS+=	tex-mathalpha>=0:../../fonts/tex-mathalpha
DEPENDS+=	tex-fontawesome5>=0:../../pkgsrc_myownpkgs/tex-fontawesome5

.include "../../print/texlive/package.mk"
.include "../../mk/bsd.pkg.mk"
