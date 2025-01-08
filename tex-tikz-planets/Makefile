# $NetBSD$

DISTNAME=	tikz-planets
PKGNAME=	tex-${DISTNAME}-1.0.2
TEXLIVE_REV=	55002
CATEGORIES=	print
MASTER_SITES=	${MASTER_SITE_TEX_CTAN:=systems/texlive/tlnet/archive/}
EXTRACT_SUFX=	.tar.xz

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://mirrors.ctan.org/systems/texlive/tlnet/archive/
COMMENT=	Illustrating solar system objects
LICENSE=	cc-by-sa-v4.0

WRKSRC=		${WRKDIR} # TODO: one of tex tlpkg, or leave it as-is
USE_LANGUAGES=	# none

.include "../../print/texlive/package.mk"
.include "../../mk/bsd.pkg.mk"
