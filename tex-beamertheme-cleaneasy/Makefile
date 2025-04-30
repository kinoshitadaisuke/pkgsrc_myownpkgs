# $NetBSD$

DISTNAME=	beamertheme-cleaneasy
PKGNAME=	tex-${DISTNAME}-1.0.3
TEXLIVE_REV=	74971
CATEGORIES=	print
MASTER_SITES=	${MASTER_SITE_TEX_CTAN:=systems/texlive/tlnet/archive/}
EXTRACT_SUFX=	.tar.xz

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://ctan.org/tex-archive/systems/texlive/tlnet/archive
COMMENT=	Beamer's theme cleaneasy
LICENSE=	public-domain

WRKSRC=		${WRKDIR} # TODO: one of tex tlpkg, or leave it as-is
USE_LANGUAGES=	# none

DEPENDS+=	tex-beamer>=0:../../print/tex-beamer

.include "../../print/texlive/package.mk"
.include "../../mk/bsd.pkg.mk"
