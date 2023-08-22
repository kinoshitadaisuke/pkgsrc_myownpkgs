# $NetBSD$

DISTNAME=	beamertheme-simpledarkblue
PKGNAME=	tex-${DISTNAME}-20210725
TEXLIVE_REV=	60061
CATEGORIES=	print
MASTER_SITES=	https://ctan.mirror.twds.com.tw/tex-archive/systems/texlive/tlnet/archive/
EXTRACT_SUFX=	.tar.xz

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://ctan.mirror.twds.com.tw/tex-archive/systems/texlive/tlnet/archive/
COMMENT=	Beamer's theme "simpledarkblue"
LICENSE=	public-domain

WRKSRC=		${WRKDIR} # TODO: one of tex tlpkg, or leave it as-is
USE_LANGUAGES=	# none

DEPENDS+=	tex-beamer>=0:../../print/tex-beamer

.include "../../print/texlive/package.mk"
.include "../../mk/bsd.pkg.mk"
