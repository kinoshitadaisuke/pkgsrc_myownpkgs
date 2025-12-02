# $NetBSD$

DISTNAME=	novabeamer-theme
PKGNAME=	tex-beamertheme-${DISTNAME:S/beamer-theme//}-1.0
TEXLIVE_REV=	76924
CATEGORIES=	print
MASTER_SITES=	https://mirrors.ctan.org/systems/texlive/tlnet/archive/
EXTRACT_SUFX=	.tar.xz

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://mirrors.ctan.org/systems/texlive/tlnet/archive/
COMMENT=	Beamer's theme nova
LICENSE=	lppl-1.3c

WRKSRC=		${WRKDIR} # TODO: one of tex tlpkg, or leave it as-is
USE_LANGUAGES=	# none

DEPENDS+=	tex-beamer>=0:../../print/tex-beamer

.include "../../print/texlive/package.mk"
.include "../../mk/bsd.pkg.mk"
