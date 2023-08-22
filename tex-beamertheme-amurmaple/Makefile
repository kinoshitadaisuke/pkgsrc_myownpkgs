# $NetBSD$

DISTNAME=	beamerthemeamurmaple
PKGNAME=	tex-${DISTNAME}-1.2
TEXLIVE_REV=	65698
CATEGORIES=	print
MASTER_SITES=	${MASTER_SITE_TEX_CTAN:=systems/texlive/tlnet/archive/}
EXTRACT_SUFX=	.tar.xz

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	http://www.dnsbalance.ring.gr.jp/pub/text/CTAN/systems/texlive/tlnet/archive/
COMMENT=	Beamer's theme amurmaple
LICENSE=	lppl-1.3c

WRKSRC=		${WRKDIR} # TODO: one of tex tlpkg, or leave it as-is
USE_LANGUAGES=	# none

DEPENDS+=	tex-beamer>=0:../../print/tex-beamer

.include "../../print/texlive/package.mk"
.include "../../mk/bsd.pkg.mk"
