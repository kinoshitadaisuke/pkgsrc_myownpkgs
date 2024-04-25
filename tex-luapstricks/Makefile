# $NetBSD$

DISTNAME=	luapstricks
PKGNAME=	tex-${DISTNAME}-20230524
TEXLIVE_REV=	67207
CATEGORIES=	print
MASTER_SITES=	https://ctan.mirror.twds.com.tw/tex-archive/systems/texlive/tlnet/archive/
EXTRACT_SUFX=	.tar.xz

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://ctan.mirror.twds.com.tw/tex-archive/systems/texlive/tlnet/archive/
COMMENT=	PSTricks backend for LuaTeX
LICENSE=	lppl-1.3c

WRKSRC=		${WRKDIR} # TODO: one of fonts tex tlpkg, or leave it as-is
USE_LANGUAGES=	# none

.include "../../print/texlive/package.mk"
.include "../../mk/bsd.pkg.mk"
