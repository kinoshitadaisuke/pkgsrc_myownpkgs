# $NetBSD$

DISTNAME=	beamerthemecelestia
PKGNAME=	tex-${DISTNAME:S/themecelestia/theme-celestia/}-1.0.1
TEXLIVE_REV=	75310
CATEGORIES=	print
MASTER_SITES=	https://mirrors.ctan.org/systems/texlive/tlnet/archive/
EXTRACT_SUFX=	.tar.xz

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://mirrors.ctan.org/systems/texlive/tlnet/archive/
COMMENT=	Modern and elegant Beamer theme for academic presentations
LICENSE=	lppl-1.3c

WRKSRC=		${WRKDIR} # TODO: one of tex tlpkg, or leave it as-is
USE_LANGUAGES=	# none

.include "../../print/texlive/package.mk"
.include "../../mk/bsd.pkg.mk"
