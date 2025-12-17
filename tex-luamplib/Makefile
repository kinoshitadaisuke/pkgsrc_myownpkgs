# $NetBSD$

DISTNAME=	luamplib
PKGNAME=	tex-${DISTNAME}-2.37.7
TEXLIVE_REV=	77027
CATEGORIES=	print
MASTER_SITES=	https://mirrors.ctan.org/systems/texlive/tlnet/archive/
EXTRACT_SUFX=	.tar.xz

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://mirrors.ctan.org/systems/texlive/tlnet/archive/
COMMENT=	LuaTeX built-in METAPOST interpreter
LICENSE=	gnu-gpl-v2

WRKSRC=		${WRKDIR} # TODO: one of tex tlpkg, or leave it as-is
USE_LANGUAGES=	# none

.include "../../print/texlive/package.mk"
.include "../../mk/bsd.pkg.mk"
