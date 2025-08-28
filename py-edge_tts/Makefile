# $NetBSD$

DISTNAME=	edge_tts-7.2.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	audio python
MASTER_SITES=	${MASTER_SITE_PYPI:=e/edge_tts/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/edge_tts/
COMMENT=	edge-tts
LICENSE=	gnu-lgpl-v3

DEPENDS+=	${PYPKGPREFIX}-aiohttp>=3.8.0,<4.0.0:../../www/py-aiohttp
DEPENDS+=	${PYPKGPREFIX}-certifi>=2023.11.17:../../security/py-certifi
DEPENDS+=	${PYPKGPREFIX}-tabulate>=0.4.4,<1.0.0:../../textproc/py-tabulate
DEPENDS+=	${PYPKGPREFIX}-typing-extensions>=4.1.0,<5.0.0:../../devel/py-typing-extensions
DEPENDS+=	${PYPKGPREFIX}-srt>=3.4.1,<4.0.0:../../pkgsrc_myownpkgs/py-srt

USE_LANGUAGES=	# none

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
