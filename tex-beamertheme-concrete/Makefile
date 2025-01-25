# $NetBSD$

DISTNAME=	beamerthemeconcrete
PKGNAME=	tex-${DISTNAME:S/themeconcrete/theme-concrete/}-2024B.2024.01.21
TEXLIVE_REV=	69528
CATEGORIES=	print
MASTER_SITES=	https://mirrors.ctan.org/systems/texlive/tlnet/archive/
EXTRACT_SUFX=	.tar.xz

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://mirrors.ctan.org/systems/texlive/tlnet/archive/
COMMENT=	Collection of flat beamer themes for academic presentations
LICENSE=	lppl-1.3c

WRKSRC=		${WRKDIR} # TODO: one of tex tlpkg, or leave it as-is
USE_LANGUAGES=	# none

.include "../../print/texlive/package.mk"
.include "../../mk/bsd.pkg.mk"
