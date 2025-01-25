# $NetBSD$

DISTNAME=	luamesh
PKGNAME=	tex-${DISTNAME}-0.7
TEXLIVE_REV=	63875
CATEGORIES=	print
MASTER_SITES=	https://mirrors.ctan.org/systems/texlive/tlnet/archive/
EXTRACT_SUFX=	.tar.xz

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://mirrors.ctan.org/systems/texlive/tlnet/archive/
COMMENT=	Computing and drawing 2D Delaunay triangulation
LICENSE=	lppl-1.3c

WRKSRC=		${WRKDIR} # TODO: one of metapost scripts tex tlpkg, or leave it as-is
USE_LANGUAGES=	# none

.include "../../print/texlive/package.mk"
.include "../../mk/bsd.pkg.mk"
