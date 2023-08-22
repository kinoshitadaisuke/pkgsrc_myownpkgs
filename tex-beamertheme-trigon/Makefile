# $NetBSD$

DISTNAME=	beamertheme-trigon
PKGNAME=	tex-${DISTNAME}-0.7.0
TEXLIVE_REV=	65985
CATEGORIES=	print
MASTER_SITES=	${MASTER_SITE_TEX_CTAN:=systems/texlive/tlnet/archive/}
EXTRACT_SUFX=	.tar.xz

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	http://www.dnsbalance.ring.gr.jp/pub/text/CTAN/systems/texlive/tlnet/archive/
COMMENT=	Beamer's theme trigon
LICENSE=	cc-by-sa-v4.0

WRKSRC=		${WRKDIR} # TODO: one of tex tlpkg, or leave it as-is
USE_LANGUAGES=	# none

DEPENDS+=	tex-beamer>=0:../../print/tex-beamer
DEPENDS+=	tex-ly1>=0:../../fonts/tex-ly1
DEPENDS+=	tex-sourcesanspro>=0:../../fonts/tex-sourcesanspro

.include "../../print/texlive/package.mk"
.include "../../mk/bsd.pkg.mk"
