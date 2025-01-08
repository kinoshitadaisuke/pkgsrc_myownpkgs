# $NetBSD$

DISTNAME=	bookcover
PKGNAME=	tex-${DISTNAME}-3.7
TEXLIVE_REV=	72461
CATEGORIES=	print
MASTER_SITES=	${MASTER_SITE_TEX_CTAN:=systems/texlive/tlnet/archive/}
EXTRACT_SUFX=	.tar.xz

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://ctan.org/tex-archive/systems/texlive/tlnet/archive/
COMMENT=	LaTeX class for making book covers and dust jackets
LICENSE=	lppl-1.2

WRKSRC=		${WRKDIR} # TODO: one of tex tlpkg, or leave it as-is
USE_LANGUAGES=	# none

.include "../../print/texlive/package.mk"
.include "../../mk/bsd.pkg.mk"
