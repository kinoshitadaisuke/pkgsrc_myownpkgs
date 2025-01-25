# $NetBSD$

DISTNAME=	beamerthemeamurmaple
PKGNAME=	tex-${DISTNAME:S/themeamurmaple/theme-amurmaple/}-1.3
TEXLIVE_REV=	69742
CATEGORIES=	print
MASTER_SITES=	${MASTER_SITE_TEX_CTAN:=systems/texlive/tlnet/archive/}
EXTRACT_SUFX=	.tar.xz

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://ctan.org/tex-archive/systems/texlive/tlnet/archive
COMMENT=	Beamer's theme amurmaple
LICENSE=	lppl-1.3c

WRKSRC=		${WRKDIR} # TODO: one of tex tlpkg, or leave it as-is
USE_LANGUAGES=	# none

DEPENDS+=	tex-beamer>=0:../../print/tex-beamer
DEPENDS+=	tex-luamesh>=0:../../pkgsrc_myownpkgs/tex-luamesh

.include "../../print/texlive/package.mk"
.include "../../mk/bsd.pkg.mk"
