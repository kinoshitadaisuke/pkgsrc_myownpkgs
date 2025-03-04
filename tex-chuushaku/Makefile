# $NetBSD$

DISTNAME=	chuushaku
PKGNAME=	tex-${DISTNAME}-1.0.1
TEXLIVE_REV=	73263
CATEGORIES=	print
MASTER_SITES=	https://mirrors.ctan.org/systems/texlive/tlnet/archive/
EXTRACT_SUFX=	.tar.xz

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://mirrors.ctan.org/systems/texlive/tlnet/archive/
COMMENT=	Flexible book notes in Japanese
LICENSE=	lppl-1.3c

WRKSRC=		${WRKDIR} # TODO: one of tex tlpkg, or leave it as-is
USE_LANGUAGES=	# none

DEPENDS+=	tex-latex>=0:../../print/tex-latex

.include "../../print/texlive/package.mk"
.include "../../mk/bsd.pkg.mk"
