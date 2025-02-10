# $NetBSD$

DISTNAME=	beamertheme-tcolorbox
PKGNAME=	tex-${DISTNAME}-0.9
TEXLIVE_REV=	73705
CATEGORIES=	print
MASTER_SITES=	${MASTER_SITE_TEX_CTAN:=systems/texlive/tlnet/archive/}
EXTRACT_SUFX=	.tar.xz

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://ctan.org/tex-archive/systems/texlive/tlnet/archive/
COMMENT=	Beamer's theme "tcolorbox"
LICENSE=	lppl-1.3c

WRKSRC=		${WRKDIR} # TODO: one of tex tlpkg, or leave it as-is
USE_LANGUAGES=	# none

DEPENDS+=	tex-beamer>=0:../../print/tex-beamer
DEPENDS+=	tex-tikzfill>=0:../../pkgsrc_myownpkgs/tex-tikzfill

.include "../../print/texlive/package.mk"
.include "../../mk/bsd.pkg.mk"
