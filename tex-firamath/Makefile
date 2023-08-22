# $NetBSD$

DISTNAME=	firamath
PKGNAME=	tex-${DISTNAME}
CATEGORIES=	fonts
MASTER_SITES=	${MASTER_SITE_TEX_CTAN:=systems/texlive/tlnet/archive/}
EXTRACT_SUFX=	.tar.xz
TEXLIVE_REV=	56672

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	http://www.dnsbalance.ring.gr.jp/pub/text/CTAN/systems/texlive/tlnet/archive/ # TODO: check
COMMENT=	firamath font
LICENSE=	lppl-1.3c

WRKSRC=		${WRKDIR} # TODO: one of fonts tlpkg, or leave it as-is
USE_LANGUAGES=	# none

.include "../../print/texlive/package.mk"
.include "../../mk/bsd.pkg.mk"
